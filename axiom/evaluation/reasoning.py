"""Reasoning evaluation suite for AXIOM."""

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class ReasoningTestResult:
    prompt: str
    response: str
    score: float


def run_reasoning_tests(prompts: Iterable[str], responses: Iterable[str]) -> List[ReasoningTestResult]:
    results: List[ReasoningTestResult] = []
    for prompt, response in zip(prompts, responses):
        score = 1.0 if response.strip() else 0.0
        results.append(ReasoningTestResult(prompt=prompt, response=response, score=score))
    return results
