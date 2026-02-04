"""Authentication utilities for the AXIOM API."""

import os
from typing import Set

from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


AUTH_SCHEME = HTTPBearer(auto_error=False)


def _load_api_keys() -> Set[str]:
    raw_keys = os.getenv("AXIOM_API_KEYS", "dev-key-axiom")
    return {key.strip() for key in raw_keys.split(",") if key.strip()}


def validate_api_key(credentials: HTTPAuthorizationCredentials | None) -> None:
    """Validate the provided API key or raise HTTP 401."""
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    if credentials.credentials not in _load_api_keys():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
