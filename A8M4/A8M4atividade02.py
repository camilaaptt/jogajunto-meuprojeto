'''

Agora, criem um scritp para:

Ter um input de usuário para inserir os números de matrícula em uma lista. 

Ter um validador nessa lista que permita a inserção de dados até ocupar 5 espaços index.

Fazer um laço de repetição para passar todos os números da lista em uma função para verificar se o número é par ou ímpar. 

'''
from A8M4atividade01 import verificaMatricula

matriculas = []

while len(matriculas) < 5:
    matricula = int(input("Digite o numero da sua matrícula: "))
    matriculas.append(matricula)

print(matriculas)

for matricula in matriculas:
    resultado = (verificaMatricula(matricula))
    print(resultado)