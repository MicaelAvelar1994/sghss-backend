from pydantic import BaseModel
from datetime import datetime

class PrescricaoBase(BaseModel):
    paciente_id: int
    profissional_id: int
    conteudo: str
    data_emissao: datetime

class PrescricaoCreate(PrescricaoBase):
    pass

class PrescricaoOut(PrescricaoBase):
    id: int
    class Config:
        orm_mode = True