from pydantic import BaseModel

class ProfissionalBase(BaseModel):
    nome: str
    especialidade: str
    registro: str

class ProfissionalCreate(ProfissionalBase):
    pass

class ProfissionalOut(ProfissionalBase):
    id: int
    class Config:
        orm_mode = True