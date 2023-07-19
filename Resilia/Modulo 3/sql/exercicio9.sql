-- O que é para fazer:

-- Você precisa selecionar dados de duas tabelas diferentes no PostgreSQL 
-- usando o comando INNER JOIN e ordenando os resultados por uma coluna específica.


SELECT * FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.id_cliente

