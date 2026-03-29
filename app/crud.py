from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Persona


def buscar_persona_por_nombre(db: Session, nombre: str) -> Persona | None:
    query = select(Persona).where(Persona.nombre.ilike(f"%{nombre.strip()}%"))
    return db.execute(query).scalars().first()
