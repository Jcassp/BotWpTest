from pydantic import BaseModel


class PersonaOut(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str
    experiencia: str
    habilidades: str
    anios_experiencia: int
    ubicacion: str
    resumen_perfil: str

    class Config:
        from_attributes = True
