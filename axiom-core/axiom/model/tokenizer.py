"""Tokenizer wrapper for AXIOM."""

from dataclasses import dataclass
from typing import Any, List


@dataclass
class TokenizationResult:
    input_ids: Any
    attention_mask: Any


class TokenizerAdapter:
    """Provides a minimal wrapper for tokenizer operations."""

    def __init__(self, tokenizer: Any) -> None:
        self.tokenizer = tokenizer

    def encode(self, text: str, add_special_tokens: bool = True) -> TokenizationResult:
        encoded = self.tokenizer(
            text,
            return_tensors="pt",
            add_special_tokens=add_special_tokens,
        )
        return TokenizationResult(
            input_ids=encoded["input_ids"],
            attention_mask=encoded.get("attention_mask"),
        )

    def decode(self, tokens: Any) -> str:
        return self.tokenizer.decode(tokens, skip_special_tokens=True)

    def batch_decode(self, tokens: Any) -> List[str]:
        return self.tokenizer.batch_decode(tokens, skip_special_tokens=True)
