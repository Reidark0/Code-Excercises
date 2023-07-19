SELECT * FROM TB_PEDIDO_PIZZA;

SELECT * FROM TB_PEDIDO;

SELECT * FROM TB_CLIENTE;

SELECT * FROM TB_PIZZA;

SELECT TBC.NOME, TBP.ID_CLIENTE, TBPP.ID_PIZZA, TBPI.NOME FROM TB_CLIENTE TBC
LEFT JOIN TB_PEDIDO TBP ON TBC.ID_CLIENTE = TBP.ID_CLIENTE
LEFT JOIN TB_PEDIDO_PIZZA TBPP ON TBPP.ID_PEDIDO = TBP.ID_PEDIDO
LEFT JOIN TB_PIZZA TBPI ON TBPI.ID_PIZZA = TBPP.ID_PIZZA
ORDER BY TBC.ID_CLIENTE;

SELECT ID_CLIENTE, SUM(PRECO) FROM TB_PEDIDO
GROUP BY ID_CLIENTE
ORDER BY ID_CLIENTE;