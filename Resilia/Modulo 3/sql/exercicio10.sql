-- O que é para fazer:

-- Você precisa selecionar dados de três tabelas diferentes no PostgreSQL 
-- usando o comando INNER JOIN e filtrando os resultados por uma condição específica.


SELECT * FROM pedidos
INNER JOIN clientes ON clientes.id = pedidos.id_cliente
INNER JOIN itens_pedidos on pedidos.id_pedido = itens_pedidos.id_pedido
WHERE clientes.id = 2728

