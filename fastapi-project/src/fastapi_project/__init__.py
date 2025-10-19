"""
FastAPI Project Package
"""
from fastapi_project.main import app

__version__ = "0.1.0"

__all__ = ["app"]


def main() -> None:
    """
    Main entry point for the application
    """
    import uvicorn
    from fastapi_project.config import settings
    
    uvicorn.run(
        "fastapi_project.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
