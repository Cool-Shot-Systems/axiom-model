"""FastAPI application entrypoint for AXIOM."""

from fastapi import FastAPI

from axiom.api.routes import router


def create_app() -> FastAPI:
    """Create and configure the AXIOM FastAPI application."""
    app = FastAPI(title="AXIOM API", version="0.2.0-dev")
    app.include_router(router)
    return app


app = create_app()
