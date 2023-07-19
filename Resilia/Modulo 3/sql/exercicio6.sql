-- O que é para fazer:

-- "Você precisa selecionar dados de duas tabelas diferentes no PostgreSQL 
-- usando o comando INNER JOIN. "

SELECT clientes.nome, pedidos.id_cliente FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.id_cliente
ORDER BY clientes.nome

