"""
Configuration module
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings
    """
    app_name: str = "FastAPI Project"
    version: str = "0.1.0"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    
    class Config:
        env_file = ".env"


settings = Settings()
