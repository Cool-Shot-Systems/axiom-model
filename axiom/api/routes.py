"""API routes for AXIOM."""

from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status

from axiom.api.auth import AUTH_SCHEME, validate_api_key
from axiom.api.schemas import GenerateRequest, GenerateResponse, HealthResponse, InfoResponse
from axiom.modeling.inference import AxiomInference, GenerationConfig
from axiom.modeling.loader import BaseModelConfig, BaseModelLoader
from axiom.prompts.generator import build_system_prompt
from axiom.utils.validators import IdentityValidator, SafetyValidator


router = APIRouter()

_inference_instance: Optional[AxiomInference] = None


def _load_identity_config() -> dict:
    import yaml

    config_path = Path(__file__).resolve().parents[1] / "config" / "identity.yaml"
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def _load_safety_config() -> dict:
    import yaml

    config_path = Path(__file__).resolve().parents[1] / "config" / "safety.yaml"
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def _load_generation_config() -> dict:
    import yaml

    config_path = Path(__file__).resolve().parents[1] / "config" / "generation.yaml"
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def _get_inference() -> AxiomInference:
    global _inference_instance
    if _inference_instance is not None:
        return _inference_instance

    identity_cfg = _load_identity_config()
    safety_cfg = _load_safety_config()
    generation_cfg = _load_generation_config()

    identity_validator = IdentityValidator(
        model_name=identity_cfg["model_name"],
        creator=identity_cfg["creator"],
        identity_statement=identity_cfg["identity_statement"],
        refusal_statement=identity_cfg["refusal_statement"],
        prohibited_mentions=identity_cfg["prohibited_mentions"],
    )
    safety_validator = SafetyValidator(blocked_topics=safety_cfg["blocked_topics"])
    generation_config = GenerationConfig(
        max_new_tokens=generation_cfg["max_new_tokens"],
        temperature=generation_cfg["temperature"],
        top_p=generation_cfg["top_p"],
        repetition_penalty=generation_cfg["repetition_penalty"],
    )

    loader = BaseModelLoader(
        BaseModelConfig(
            model_path=Path(generation_cfg["model_path"]),
            tokenizer_path=Path(generation_cfg.get("tokenizer_path") or generation_cfg["model_path"]),
            device=generation_cfg.get("device", "cpu"),
            dtype=generation_cfg.get("dtype"),
            trust_remote_code=generation_cfg.get("trust_remote_code", False),
        )
    )
    artifacts = loader.load()
    _inference_instance = AxiomInference(
        model=artifacts.model,
        tokenizer=artifacts.tokenizer,
        identity_validator=identity_validator,
        safety_validator=safety_validator,
        generation_config=generation_config,
    )
    return _inference_instance


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", model="AXIOM", owner="Cool Shot Systems")


@router.get("/v1/info", response_model=InfoResponse, dependencies=[Depends(AUTH_SCHEME)])
def info(credentials=Depends(AUTH_SCHEME)) -> InfoResponse:
    validate_api_key(credentials)
    return InfoResponse(
        name="AXIOM",
        version="0.2.0-dev",
        company="Cool Shot Systems",
        status="development",
    )


@router.post("/v1/generate", response_model=GenerateResponse, dependencies=[Depends(AUTH_SCHEME)])
def generate(request: GenerateRequest, credentials=Depends(AUTH_SCHEME)) -> GenerateResponse:
    validate_api_key(credentials)
    try:
        identity_cfg = _load_identity_config()
        system_prompt = build_system_prompt(identity_cfg["identity_statement"])
        inference = _get_inference()
        result = inference.generate(prompt=request.prompt, system_prompt=system_prompt)
    except Exception as exc:  # pragma: no cover - defensive error handling
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Generation failed",
        ) from exc
    return GenerateResponse(model="AXIOM", response=result["response"])
