"""Dataset utilities for AXIOM."""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List


@dataclass
class JsonlExample:
    prompt: str
    response: str
    metadata: Dict[str, str]


def load_jsonl(path: Path) -> List[JsonlExample]:
    examples: List[JsonlExample] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            examples.append(
                JsonlExample(
                    prompt=record["prompt"],
                    response=record["response"],
                    metadata=record.get("metadata", {}),
                )
            )
    return examples


def iter_training_text(examples: Iterable[JsonlExample]) -> Iterable[str]:
    for example in examples:
        yield f"User: {example.prompt}\nAXIOM: {example.response}"
