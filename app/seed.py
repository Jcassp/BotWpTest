from sqlalchemy.orm import Session

from .models import Persona

SAMPLE_PERSONAS = [
    {
        "nombre": "Juan Perez",
        "telefono": "+52 55 1000 2000",
        "email": "juan.perez@example.com",
        "experiencia": "5 años en logística y atención al cliente.",
        "habilidades": "Excel, CRM, SAP",
        "anios_experiencia": 5,
        "ubicacion": "CDMX",
        "resumen_perfil": "Perfil orientado a operaciones, servicio y mejora continua.",
    },
    {
        "nombre": "María López",
        "telefono": "+52 81 3000 4000",
        "email": "maria.lopez@example.com",
        "experiencia": "3 años como analista de datos en e-commerce.",
        "habilidades": "Python, SQL, Power BI",
        "anios_experiencia": 3,
        "ubicacion": "Monterrey",
        "resumen_perfil": "Analítica de negocio con foco en métricas y automatización.",
    },
]


def seed_personas(db: Session) -> None:
    if db.query(Persona).first():
        return

    for item in SAMPLE_PERSONAS:
        db.add(Persona(**item))

    db.commit()
