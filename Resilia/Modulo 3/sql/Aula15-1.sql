CREATE TABLE FUNCIONARIO(
	ID SERIAL PRIMARY KEY,
	NOME VARCHAR(100),
	PROFISSAO VARCHAR(100),
	DATA_NASCIMENTO DATE
)

CREATE TABLE FUNCIONARIO_AUDITORIA(
	ID_FUNCIONARIO INTEGER
	NOME VARCHAR
	MODIFICACAO TIMESTAMP
)