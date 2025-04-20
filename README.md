# SGHSS Backend – Sistema de Gestão Hospitalar e de Serviços de Saúde

Este é o back-end do **SGHSS (Sistema de Gestão Hospitalar e de Serviços de Saúde)**, desenvolvido para atender as necessidades da instituição **VidaPlus**, que administra hospitais, clínicas, laboratórios e equipes de home care.

O sistema foi projetado para gerenciar dados de pacientes, profissionais de saúde, administração hospitalar e recursos de telemedicina, com foco em segurança, desempenho, escalabilidade e conformidade com a LGPD.

---

##  Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI** – para criação da API RESTful
- **SQLite** – banco de dados relacional leve
- **SQLAlchemy** – ORM para manipulação do banco
- **Pydantic** – validação de dados
- **Uvicorn** – servidor ASGI para rodar a aplicação
- **Alembic** – controle de migrações de banco de dados (em breve)

---

##  Funcionalidades Principais

###  Profissionais de Saúde
- Cadastro de médicos, enfermeiros e técnicos
- Gerenciamento de agendas
- Edição de prontuários e prescrições

###  Pacientes
- Cadastro e visualização de dados
- Agendamento e cancelamento de consultas
- Histórico médico
- Acesso à teleconsulta

###  Administração Hospitalar
- Controle de leitos
- Gestão de suprimentos
- Relatórios financeiros e operacionais

###  Telemedicina
- Videochamadas seguras (a implementar)
- Registro online de consultas e prescrições

###  Segurança e Compliance
- Criptografia de dados sensíveis
- Controle de acesso por perfil (Admin, Médico, Paciente)
- Registro de logs e conformidade com a **LGPD**

---

##  Estrutura do Projeto
ghss-backend/ 
│ ├── app/
│ ├── main.py # Ponto de entrada da API 
│ ├── models/ # Modelos de dados (ORM) 
│ ├── schemas/ # Schemas Pydantic 
│ ├── crud/ # Operações de banco de dados 
│ └── routers/ # Rotas organizadas por domínio 
│ ├── database/ 
│ ├── database.py # Conexão e inicialização do banco 
│ ├── requirements.txt # Dependências do projeto 
├── README.md # Este arquivo 
    └── sghss.sql # Script de criação do banco

