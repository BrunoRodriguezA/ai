# FastAPI Project

API REST creada con FastAPI y gestionada con UV.

## 📋 Requisitos Previos

- Python 3.13 o superior
- UV (gestor de paquetes y entornos virtuales)

## 🚀 Instalación de UV

Si aún no tienes UV instalado, ejecuta:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Luego agrega UV a tu PATH:

```bash
source $HOME/.local/bin/env
```

## 📦 Configuración del Proyecto

### 1. Clonar o navegar al proyecto

```bash
cd fastapi-project
```

### 2. Instalar dependencias

UV automáticamente creará un entorno virtual y instalará las dependencias:

```bash
uv sync
```

### 3. Configurar variables de entorno (opcional)

Copia el archivo de ejemplo y ajusta según tus necesidades:

```bash
cp .env.example .env
```

## 🏃 Comandos Principales

### Ejecutar el servidor de desarrollo

```bash
# Opción 1: Usando el script definido
uv run fastapi-project

# Opción 2: Usando uvicorn directamente
uv run uvicorn fastapi_project.main:app --reload --host 0.0.0.0 --port 8000
```

### Agregar nuevas dependencias

```bash
# Agregar una dependencia
uv add nombre-paquete

# Agregar una dependencia de desarrollo
uv add --dev nombre-paquete
```

### Actualizar dependencias

```bash
uv sync --upgrade
```

### Ver dependencias instaladas

```bash
uv pip list
```

## 📁 Estructura del Proyecto

```
fastapi-project/
├── src/
│   └── fastapi_project/
│       ├── __init__.py          # Punto de entrada principal
│       ├── main.py              # Aplicación FastAPI
│       ├── config.py            # Configuración de la aplicación
│       └── routers/             # Rutas de la API
│           ├── __init__.py
│           └── health.py        # Endpoint de health check
├── .env.example                 # Ejemplo de variables de entorno
├── .gitignore                   # Archivos ignorados por git
├── pyproject.toml               # Configuración del proyecto y dependencias
└── README.md                    # Este archivo
```

## 🔗 Endpoints Disponibles

Una vez que el servidor esté corriendo, puedes acceder a:

- **API Root**: http://localhost:8000/
- **Health Check**: http://localhost:8000/health
- **Documentación interactiva (Swagger UI)**: http://localhost:8000/docs
- **Documentación alternativa (ReDoc)**: http://localhost:8000/redoc

## 🛠️ Desarrollo

### Agregar un nuevo router

1. Crea un nuevo archivo en `src/fastapi_project/routers/`:

```python
# src/fastapi_project/routers/users.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("")
async def list_users():
    return {"users": []}
```

2. Importa y registra el router en `main.py`:

```python
from fastapi_project.routers import health, users

app.include_router(health.router)
app.include_router(users.router)
```

## 📚 Dependencias Principales

- **FastAPI**: Framework web moderno y rápido
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Pydantic**: Validación de datos y configuración
- **Pydantic Settings**: Gestión de configuración desde variables de entorno

## 🧪 Testing (próximamente)

```bash
# Agregar pytest
uv add --dev pytest pytest-asyncio httpx

# Ejecutar tests
uv run pytest
```

## 📝 Notas Adicionales

- El servidor se recarga automáticamente cuando detecta cambios en el código (modo desarrollo)
- La documentación de la API se genera automáticamente usando OpenAPI
- CORS está habilitado para todos los orígenes (ajustar para producción)

## 🤝 Contribuir

1. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
2. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
3. Push a la rama (`git push origin feature/AmazingFeature`)
4. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
