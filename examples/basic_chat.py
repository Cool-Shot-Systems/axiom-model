"""Simple chat example for AXIOM."""

from pathlib import Path

import yaml

from axiom.modeling.inference import AxiomInference, GenerationConfig
from axiom.modeling.loader import BaseModelConfig, BaseModelLoader
from axiom.prompts.generator import build_system_prompt
from axiom.utils.validators import IdentityValidator, SafetyValidator


def main() -> None:
    identity_cfg = yaml.safe_load(Path("axiom/config/identity.yaml").read_text(encoding="utf-8"))
    safety_cfg = yaml.safe_load(Path("axiom/config/safety.yaml").read_text(encoding="utf-8"))
    generation_cfg = yaml.safe_load(Path("axiom/config/generation.yaml").read_text(encoding="utf-8"))
    system_prompt = build_system_prompt(identity_cfg["identity_statement"])

    loader = BaseModelLoader(BaseModelConfig(model_path=Path("/path/to/base/model")))
    artifacts = loader.load()

    identity_validator = IdentityValidator(
        model_name=identity_cfg["model_name"],
        creator=identity_cfg["creator"],
        identity_statement=identity_cfg["identity_statement"],
        refusal_statement=identity_cfg["refusal_statement"],
        prohibited_mentions=identity_cfg["prohibited_mentions"],
    )
    safety_validator = SafetyValidator(blocked_topics=safety_cfg["blocked_topics"])

    inference = AxiomInference(
        model=artifacts.model,
        tokenizer=artifacts.tokenizer,
        identity_validator=identity_validator,
        safety_validator=safety_validator,
        generation_config=GenerationConfig(**generation_cfg),
    )

    prompt = "Hello, AXIOM"
    result = inference.generate(prompt, system_prompt)
    print(result["response"])


if __name__ == "__main__":
    main()
