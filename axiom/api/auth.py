"""Authentication utilities for the AXIOM API."""

from typing import Set

from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


AUTH_SCHEME = HTTPBearer(auto_error=False)
ALLOWED_API_KEYS: Set[str] = {"dev-key-axiom"}


def validate_api_key(credentials: HTTPAuthorizationCredentials | None) -> None:
    """Validate the provided API key or raise HTTP 401."""
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    if credentials.credentials not in ALLOWED_API_KEYS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
