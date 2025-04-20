from pydantic import BaseModel
from datetime import datetime

class ConsultaBase(BaseModel):
    paciente_id: int
    profissional_id: int
    data_hora: datetime
    observacoes: str = ""

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaOut(ConsultaBase):
    id: int
    class Config:
        orm_mode = True