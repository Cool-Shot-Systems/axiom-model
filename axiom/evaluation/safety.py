"""Safety evaluation suite for AXIOM."""

from dataclasses import dataclass
from typing import Iterable, List

from axiom.utils.validators import SafetyValidator


@dataclass
class SafetyTestResult:
    prompt: str
    allowed: bool


def run_safety_tests(prompts: Iterable[str], validator: SafetyValidator) -> List[SafetyTestResult]:
    results: List[SafetyTestResult] = []
    for prompt in prompts:
        results.append(SafetyTestResult(prompt=prompt, allowed=validator.is_prompt_allowed(prompt)))
    return results
