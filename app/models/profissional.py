from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Profissional(Base):
    __tablename__ = "profissionais"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)
    registro = Column(String, unique=True, nullable=False)