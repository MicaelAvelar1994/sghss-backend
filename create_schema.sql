CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    telefone TEXT
);
CREATE TABLE profissionais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT,
    registro TEXT UNIQUE NOT NULL
);
CREATE TABLE consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    profissional_id INTEGER NOT NULL,
    data_hora DATETIME NOT NULL,
    observacoes TEXT,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY(profissional_id) REFERENCES profissionais(id)
);
CREATE TABLE internacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    leito_numero INTEGER NOT NULL,
    data_entrada DATETIME NOT NULL,
    data_saida DATETIME,
    ativa BOOLEAN DEFAULT 1,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
);
CREATE TABLE prescricoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    profissional_id INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    data_emissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY(profissional_id) REFERENCES profissionais(id)
);