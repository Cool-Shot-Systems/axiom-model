"""Identity and safety validators for AXIOM."""

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class IdentityValidator:
    model_name: str
    creator: str
    identity_statement: str
    refusal_statement: str
    prohibited_mentions: List[str]

    def is_identity_compliant(self, response: str) -> bool:
        response_lower = response.lower()
        if self.model_name.lower() not in response_lower:
            return False
        if self.creator.lower() not in response_lower:
            return False
        for term in self.prohibited_mentions:
            if term.lower() in response_lower:
                return False
        return True


@dataclass
class SafetyValidator:
    blocked_topics: Iterable[str]

    def is_prompt_allowed(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()
        return not any(topic.lower() in prompt_lower for topic in self.blocked_topics)
