'''
Mini Case 2: Notas dos alunos

Desafio: Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.

O que seu programa deve conter:

Um input onde cada interação tenha um texto.
No final, seu programa deverá ter o output:
“Olá, Caique! Sua média é: 10 pontos”

'''

nomeUsuario = input('Digite o seu nome: ')
n1 = float(input('Digite a sua nota da primeira avaliação: '))
n2 = float(input('Digite a sua nota da segunda avaliação: '))
n3 = float(input('Digite a sua nota da terceira avaliação: '))
n4 = float(input('Digite a sua nota da quarta avaliação: '))

media = ((n1 + n2 + n3 + n4)/4)

print(f"Olá, {nomeUsuario}! Sua média é: {media} pontos.")