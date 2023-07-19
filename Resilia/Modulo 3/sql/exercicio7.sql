-- O que é para fazer:

-- Você precisa selecionar dados de duas tabelas diferentes no PostgreSQL 
-- usando o comando INNER JOIN e aplicando uma condição de filtro na junção das tabelas.




SELECT * FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.id_cliente
WHERE clientes.id = 27


