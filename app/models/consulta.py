from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Consulta(Base):
    __tablename__ = "consultas"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    profissional_id = Column(Integer, ForeignKey("profissionais.id"))
    data_hora = Column(DateTime, default=datetime.utcnow)
    observacoes = Column(Text)

    paciente = relationship("Paciente")
    profissional = relationship("Profissional")