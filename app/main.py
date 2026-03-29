from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .crud import buscar_persona_por_nombre
from .database import Base, SessionLocal, engine
from .schemas import PersonaOut
from .seed import seed_personas

app = FastAPI(title="Mini Bot WhatsApp - Perfiles")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_personas(db)
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/buscar", response_model=PersonaOut)
def buscar(nombre: str, db: Session = Depends(get_db)):
    persona = buscar_persona_por_nombre(db, nombre)
    if not persona:
        raise HTTPException(status_code=404, detail="No se encontró una persona con ese nombre")
    return persona


@app.post("/webhook")
def webhook(payload: dict, db: Session = Depends(get_db)) -> dict[str, str]:
    mensaje = str(payload.get("mensaje", "")).strip()

    if not mensaje:
        return {"respuesta": "Mensaje vacío. Usa: buscar <nombre>."}

    if not mensaje.lower().startswith("buscar "):
        return {"respuesta": "Comando no reconocido. Usa: buscar <nombre>."}

    nombre = mensaje[7:].strip()
    if not nombre:
        return {"respuesta": "Falta el nombre. Ejemplo: buscar Juan Perez"}

    persona = buscar_persona_por_nombre(db, nombre)
    if not persona:
        return {"respuesta": f"No encontré perfiles para: {nombre}"}

    respuesta = (
        "Perfil encontrado:\n"
        f"Nombre: {persona.nombre}\n"
        f"Experiencia: {persona.experiencia}\n"
        f"Habilidades: {persona.habilidades}\n"
        f"Ubicación: {persona.ubicacion}"
    )
    return {"respuesta": respuesta}
