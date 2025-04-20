from pydantic import BaseModel

class PacienteBase(BaseModel):
    nome: str
    idade: int
    cpf: str
    telefone: str | None = None

class PacienteCreate(PacienteBase):
    pass

class PacienteOut(PacienteBase):
    id: int
    class Config:
        orm_mode = True