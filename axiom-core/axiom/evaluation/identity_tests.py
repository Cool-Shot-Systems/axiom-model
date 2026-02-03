"""Identity evaluation suite for AXIOM."""

from dataclasses import dataclass
from typing import Iterable, List

from axiom.utils.validators import IdentityValidator


@dataclass
class IdentityTestResult:
    prompt: str
    response: str
    passed: bool


def run_identity_tests(
    prompts: Iterable[str],
    responses: Iterable[str],
    validator: IdentityValidator,
) -> List[IdentityTestResult]:
    results: List[IdentityTestResult] = []
    for prompt, response in zip(prompts, responses):
        results.append(
            IdentityTestResult(
                prompt=prompt,
                response=response,
                passed=validator.is_identity_compliant(response),
            )
        )
    return results
