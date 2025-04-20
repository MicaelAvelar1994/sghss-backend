from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Internacao(Base):
    __tablename__ = "internacoes"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    leito_numero = Column(Integer, nullable=False)
    data_entrada = Column(DateTime, default=datetime.utcnow)
    data_saida = Column(DateTime, nullable=True)
    ativa = Column(Boolean, default=True)

    paciente = relationship("Paciente")