# ⚡ Inicio Rápido - FastAPI Project

## 🎯 Para Empezar en 3 Pasos

### 1️⃣ Instalar UV (si no lo tienes)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

### 2️⃣ Instalar Dependencias

```bash
cd fastapi-project
uv sync
```

### 3️⃣ Ejecutar el Servidor

```bash
uv run fastapi-project
```

¡Listo! Abre tu navegador en:
- 🌐 **API**: http://localhost:8000
- 📚 **Documentación**: http://localhost:8000/docs

---

## 🔥 Comandos Más Usados

```bash
# Ejecutar servidor de desarrollo
uv run fastapi-project

# Ejecutar con reload automático
uv run uvicorn fastapi_project.main:app --reload

# Agregar una nueva dependencia
uv add nombre-del-paquete

# Actualizar dependencias
uv sync --upgrade

# Ver dependencias instaladas
uv pip list
```

---

## 📁 Estructura del Proyecto

```
src/fastapi_project/
├── __init__.py      # Punto de entrada
├── main.py          # Aplicación FastAPI principal
├── config.py        # Configuración
└── routers/         # Endpoints de la API
    ├── __init__.py
    └── health.py    # Health check
```

---

## ➕ Agregar un Nuevo Endpoint

1. **Crea un router** en `src/fastapi_project/routers/mi_router.py`:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/mi-ruta", tags=["Mi Tag"])

@router.get("")
async def mi_endpoint():
    return {"mensaje": "Hola!"}
```

2. **Regístralo** en `src/fastapi_project/main.py`:

```python
from fastapi_project.routers import health, mi_router

app.include_router(health.router)
app.include_router(mi_router.router)
```

3. **¡Eso es todo!** El servidor con `--reload` detectará los cambios automáticamente.

---

## 🆘 Problemas Comunes

### "uv: command not found"
```bash
source $HOME/.local/bin/env
```

### Reinstalar dependencias
```bash
rm -rf .venv
uv sync
```

### Puerto en uso
```bash
# Cambia el puerto en config.py o usa:
uv run uvicorn fastapi_project.main:app --reload --port 8001
```

---

## 📖 Más Información

- Ver `README.md` para documentación completa
- Ver `COMANDOS.md` para todos los comandos disponibles
- Visita `/docs` en tu servidor para explorar la API interactivamente
