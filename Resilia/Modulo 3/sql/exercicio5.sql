-- O que é para fazer:

-- Crie uma tabela avançada chamada "funcionarios" com as seguintes colunas: 
-- "id" (inteiro), 
-- "nome" (texto), 
-- "idade" (inteiro), 
-- "salario" (decimal), 
-- "departamento" (texto) e 
-- "data_contratacao" (data).

CREATE TABLE funcionarios(
    id SERIAL PRIMARY KEY,
    nome VARCHAR,
    idade INTEGER,
    salario FLOAT,
    departamento VARCHAR,
    data_contratacao DATE
);
