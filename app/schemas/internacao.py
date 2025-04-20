from pydantic import BaseModel
from datetime import datetime

class InternacaoBase(BaseModel):
    paciente_id: int
    leito_numero: int
    data_entrada: datetime
    data_saida: datetime | None = None
    ativa: bool = True

class InternacaoCreate(InternacaoBase):
    pass

class InternacaoOut(InternacaoBase):
    id: int
    class Config:
        orm_mode = True