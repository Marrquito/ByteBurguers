# ByteBurguers
Trabalho da cadeira Banco de Dados I

# Mini doc back-end
o sistema vai funcionar com o cadastro de mesas, usuarios e itens no menu

apos isso começamos o cadastro de pedidos, ao criar um pedido so passara o id_usuario, id_mesa
ao cadastrar um pedido a mesa automaticamente ficara marcada como ocupada 
nao é permitido cadastrar um pedido a uma mesa que ja estava ocupada

apos isso so cadastramos na tabela itemsOrdered, passando o id do pedido, quantidade de itens e o id do item
ele checa se tem item suficiente e se tem remove a quantidade comprada do estoque
apos isso repetimos esse processo de cadastro de itens pedidos ate a hora de fechar a conta

ao fechar a conta passamos o id do pedido e o metodo de pagamento como "cartao, dinheiro, berry, etc" e ele vai calcular o valor total da conta e liberar a mesa atrelada ao pedido
dando o desconto de 20% se o cliente torcer flamengo ou assistir one_piece
alem de retornar todos os dados daquele pedido