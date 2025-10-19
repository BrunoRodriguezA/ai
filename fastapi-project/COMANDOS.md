# 📝 Comandos Rápidos - FastAPI Project

## 🔧 Comandos Esenciales con UV

### Instalación y Configuración

```bash
# Instalar UV (si no lo tienes)
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Inicializar un nuevo proyecto
uv init mi-proyecto --package

# Sincronizar dependencias (instalar/actualizar)
uv sync
```

### Gestión de Dependencias

```bash
# Agregar una dependencia
uv add fastapi uvicorn[standard]

# Agregar dependencia de desarrollo
uv add --dev pytest

# Eliminar una dependencia
uv remove nombre-paquete

# Ver dependencias instaladas
uv pip list

# Actualizar todas las dependencias
uv sync --upgrade

# Actualizar una dependencia específica
uv add --upgrade nombre-paquete
```

### Ejecución del Proyecto

```bash
# Ejecutar usando el script definido en pyproject.toml
uv run fastapi-project

# Ejecutar con uvicorn directamente (desarrollo)
uv run uvicorn fastapi_project.main:app --reload

# Ejecutar con host y puerto específicos
uv run uvicorn fastapi_project.main:app --reload --host 0.0.0.0 --port 8000

# Ejecutar en modo producción (sin reload)
uv run uvicorn fastapi_project.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Ejecutar Scripts Python

```bash
# Ejecutar cualquier script Python
uv run python mi_script.py

# Ejecutar módulo
uv run python -m mi_modulo
```

### Entorno Virtual

```bash
# UV crea automáticamente un .venv, pero si necesitas activarlo manualmente:

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Desactivar
deactivate
```

## 🧪 Testing (cuando se agregue pytest)

```bash
# Instalar dependencias de testing
uv add --dev pytest pytest-asyncio httpx

# Ejecutar tests
uv run pytest

# Ejecutar con cobertura
uv run pytest --cov=fastapi_project

# Ejecutar tests específicos
uv run pytest tests/test_main.py
```

## 📊 Comandos de Desarrollo

```bash
# Verificar el proyecto
uv run python -c "from fastapi_project import app; print('OK')"

# Ver información del proyecto
uv pip show fastapi-project

# Exportar dependencias a requirements.txt (si es necesario)
uv pip compile pyproject.toml -o requirements.txt
```

## 🔍 Inspección y Debug

```bash
# Ver la configuración actual de UV
uv --version

# Ver el árbol de dependencias
uv pip tree

# Verificar problemas con dependencias
uv pip check
```

## 🌐 URLs del Servidor Local

Cuando el servidor esté corriendo:

- **API Root**: http://localhost:8000/
- **Health Check**: http://localhost:8000/health
- **Swagger UI (Documentación Interactiva)**: http://localhost:8000/docs
- **ReDoc (Documentación Alternativa)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🚀 Despliegue

```bash
# Generar archivo de bloqueo de dependencias
uv lock

# Instalar dependencias en producción (sin dev)
uv sync --no-dev

# Ejecutar en modo producción
uv run uvicorn fastapi_project.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📦 Construcción y Distribución

```bash
# Construir el paquete
uv build

# Instalar el paquete localmente
uv pip install .

# Instalar en modo editable (desarrollo)
uv pip install -e .
```

## 🛠️ Comandos Útiles Adicionales

```bash
# Limpiar caché de UV
uv cache clean

# Ver información de UV
uv --help

# Ejecutar con variables de entorno
uv run --env-file .env python mi_script.py

# Python REPL con el entorno del proyecto
uv run python
```

## 💡 Tips

1. **No necesitas activar el entorno virtual**: `uv run` lo hace automáticamente
2. **Actualiza regularmente**: `uv sync --upgrade` mantiene tus dependencias al día
3. **Usa `.env` para configuración**: Variables de entorno para diferentes ambientes
4. **Documentación automática**: FastAPI genera docs automáticamente en `/docs`
5. **Hot reload**: El flag `--reload` reinicia el servidor al detectar cambios

## 🔗 Recursos

- [Documentación de UV](https://github.com/astral-sh/uv)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Uvicorn](https://www.uvicorn.org/)
