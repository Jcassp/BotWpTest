# BotWpTest - Mini proyecto bot WhatsApp (práctica)

Este proyecto es una base mínima para practicar un bot que responde perfiles de personas desde una base de datos.

## Stack

- Python 3.11+
- FastAPI
- SQLite (archivo local `personas.db`)
- SQLAlchemy

## ¿Qué hace?

- `GET /health` para validar que la API está viva.
- `GET /buscar?nombre=...` para buscar un perfil por nombre.
- `POST /webhook` para simular el mensaje de WhatsApp.

## Instalación y ejecución

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Prueba rápida

### 1) Buscar por endpoint

```bash
curl "http://127.0.0.1:8000/buscar?nombre=Juan"
```

### 2) Simular mensaje de bot

```bash
curl -X POST "http://127.0.0.1:8000/webhook" \
  -H "Content-Type: application/json" \
  -d '{"mensaje":"buscar Maria"}'
```

## Próximos pasos

1. Cambiar SQLite por PostgreSQL.
2. Agregar autenticación.
3. Integrar webhook real de WhatsApp Cloud API.
