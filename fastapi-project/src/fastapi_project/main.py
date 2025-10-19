"""
FastAPI Application Main Module
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_project.routers import health

# Create FastAPI app instance
app = FastAPI(
    title="FastAPI Project",
    description="API REST creada con FastAPI",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configurar según necesidades de producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router)


@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {
        "message": "¡Bienvenido a la API de FastAPI!",
        "version": "0.1.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }
