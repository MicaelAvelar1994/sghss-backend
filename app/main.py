from fastapi import FastAPI
from app.routers import pacientes, profissionais, consultas, internacoes, prescricoes

app = FastAPI(title="SGHSS - Sistema de Gestão Hospitalar e Serviços de Saúde")

app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(profissionais.router, prefix="/profissionais", tags=["Profissionais"])
app.include_router(consultas.router, prefix="/consultas", tags=["Consultas"])
app.include_router(internacoes.router, prefix="/internacoes", tags=["Internações"])
app.include_router(prescricoes.router, prefix="/prescricoes", tags=["Prescrições"])