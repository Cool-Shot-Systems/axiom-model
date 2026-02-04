"""Pydantic schemas for the AXIOM API."""

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Request payload for text generation."""

    prompt: str = Field(..., min_length=1)
    max_tokens: int = Field(150, ge=1, le=2048)


class GenerateResponse(BaseModel):
    """Response payload for text generation."""

    model: str
    response: str


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    model: str
    owner: str


class InfoResponse(BaseModel):
    """Model info response."""

    name: str
    version: str
    company: str
    status: str
