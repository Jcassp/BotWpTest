from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Persona(Base):
    __tablename__ = "personas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(120), index=True)
    telefono: Mapped[str] = mapped_column(String(40), default="")
    email: Mapped[str] = mapped_column(String(120), default="")
    experiencia: Mapped[str] = mapped_column(Text)
    habilidades: Mapped[str] = mapped_column(Text)
    anios_experiencia: Mapped[int] = mapped_column(Integer, default=0)
    ubicacion: Mapped[str] = mapped_column(String(120), default="")
    resumen_perfil: Mapped[str] = mapped_column(Text, default="")
