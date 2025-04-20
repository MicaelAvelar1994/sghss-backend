from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Prescricao(Base):
    __tablename__ = "prescricoes"
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    profissional_id = Column(Integer, ForeignKey("profissionais.id"))
    conteudo = Column(Text, nullable=False)
    data_emissao = Column(DateTime, default=datetime.utcnow)

    paciente = relationship("Paciente")
    profissional = relationship("Profissional")