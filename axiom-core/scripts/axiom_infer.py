#!/usr/bin/env python
"""Run AXIOM inference from the command line."""

import argparse
from pathlib import Path

import yaml

from axiom.modeling.inference import AxiomInference, GenerationConfig
from axiom.modeling.loader import BaseModelConfig, BaseModelLoader
from axiom.prompts.generator import build_system_prompt
from axiom.utils.validators import IdentityValidator, SafetyValidator


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run AXIOM inference")
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    identity_cfg = load_yaml(Path("axiom/config/identity.yaml"))
    generation_cfg = load_yaml(Path("axiom/config/generation.yaml"))
    safety_cfg = load_yaml(Path("axiom/config/safety.yaml"))
    system_prompt = build_system_prompt(identity_cfg["identity_statement"])

    identity_validator = IdentityValidator(
        model_name=identity_cfg["model_name"],
        creator=identity_cfg["creator"],
        identity_statement=identity_cfg["identity_statement"],
        refusal_statement=identity_cfg["refusal_statement"],
        prohibited_mentions=identity_cfg["prohibited_mentions"],
    )
    safety_validator = SafetyValidator(blocked_topics=safety_cfg["blocked_topics"])

    loader = BaseModelLoader(BaseModelConfig(model_path=args.model_path, device=args.device))
    artifacts = loader.load()

    generation = GenerationConfig(**generation_cfg)
    inference = AxiomInference(
        model=artifacts.model,
        tokenizer=artifacts.tokenizer,
        identity_validator=identity_validator,
        safety_validator=safety_validator,
        generation_config=generation,
    )

    result = inference.generate(args.prompt, system_prompt)
    print(result["response"])


if __name__ == "__main__":
    main()
