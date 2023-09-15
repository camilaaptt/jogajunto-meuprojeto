'''
Crie um script com as seguintes instruções, pesquisando na internet como fazer:

- Crie uma tupla com 5 dados
- Altere a tupla para uma lista
- Insira 2 dados extras a essa lista
- Remova o primeiro dado da lista
- Remova o último dado da lista
- Faça um print com o primeiro dado da lista
- Faça um print com a quantidade de dados da lista
- Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
- Imprima somente o valor contido na chave Nome do dicionário

'''

# Crie uma tupla com 5 dados
tuplaCores = ('vermelha', 'laranja', 'amarela', 'verde', 'azul')
print(tuplaCores)

# Altere a tupla para uma lista
listaCores = list(tuplaCores)
print(listaCores)

# Insira 2 dados extras a essa lista
listaCores.extend(['anil', 'violeta'])
print(listaCores)

# Remova o primeiro dado da lista
listaCores.remove('vermelha')
print(listaCores)

# Remova o último dado da lista
listaCores.pop()
print(listaCores)

# Faça um print com o primeiro dado da lista
print("O primeiro dado da lista é:", listaCores[0])

# Faça um print com a quantidade de dados da lista
print("A quantidade de dados na lista é:", len(listaCores))

# Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
dicionario = {
    "nome": 'Camila',
    "idade": 33,
    "profissao": 'Analista de Testes' 
}

# Imprima somente o valor contido na chave Nome do dicionário
print(dicionario['nome'])

### FIM ###