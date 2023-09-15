'''
Leiam o caso abaixo e executem usando Python.

A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:

Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10.
'''

nomeCliente = 'PAULA'
sobrenomeCliente = 'MARTINS'
mesCompra = 'JANEIRO'
valorCompra = '500,00'
desconto = '10'

print('Olá, ' + nomeCliente + ' ' + sobrenomeCliente + '. Em ' + mesCompra + ' você realizou uma compra no valor de R$' + valorCompra + ' e ganhou um desconto de ' + desconto + '% em sua próxima compra. Use o cupom ' + nomeCliente +'É' + desconto + '.')
