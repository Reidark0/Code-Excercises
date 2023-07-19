-- O que é para fazer:

-- Você precisa selecionar dados de três tabelas diferentes no PostgreSQL 
-- usando o comando INNER JOIN e agrupando os resultados por uma coluna específica.



SELECT pedidos.id_pedido, COUNT(itens_pedidos.id_produto) FROM pedidos
INNER JOIN clientes ON clientes.id = pedidos.id_cliente
INNER JOIN itens_pedidos on pedidos.id_pedido = itens_pedidos.id_pedido
GROUP BY id_pedido