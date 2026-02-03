"""Model loading abstractions for AXIOM."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


@dataclass
class ModelArtifacts:
    model: Any
    tokenizer: Any


@dataclass
class BaseModelConfig:
    model_path: Path
    tokenizer_path: Optional[Path] = None
    device: str = "cpu"
    dtype: Optional[str] = None
    trust_remote_code: bool = False


class BaseModelLoader:
    """Loads a base text model and tokenizer from local paths."""

    def __init__(self, config: BaseModelConfig) -> None:
        self.config = config

    def load(self) -> ModelArtifacts:
        tokenizer_path = self.config.tokenizer_path or self.config.model_path
        model, tokenizer = self._load_transformer_artifacts(
            model_path=self.config.model_path,
            tokenizer_path=tokenizer_path,
            device=self.config.device,
            dtype=self.config.dtype,
            trust_remote_code=self.config.trust_remote_code,
        )
        return ModelArtifacts(model=model, tokenizer=tokenizer)

    def _load_transformer_artifacts(
        self,
        model_path: Path,
        tokenizer_path: Path,
        device: str,
        dtype: Optional[str],
        trust_remote_code: bool,
    ) -> Tuple[Any, Any]:
        from transformers import AutoModelForCausalLM, AutoTokenizer

        model_kwargs: Dict[str, Any] = {"trust_remote_code": trust_remote_code}
        if dtype:
            import torch

            model_kwargs["torch_dtype"] = getattr(torch, dtype)

        model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, trust_remote_code=trust_remote_code)
        model.to(device)
        model.eval()
        return model, tokenizer
