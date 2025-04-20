from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String)