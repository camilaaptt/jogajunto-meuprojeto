'''
ATIVIDADE:

PARTE 2

EM SQUAD

Crie a estrutura de uma tabuada para um valor inserido. O resultado deverá ser printado do valor multiplicado de 1 a 10.  
   
'''

numero = int(input("Digite um número: "))

print('-'*30)
print(f'TABUADA DO {numero}')
print('-'*30)
for i in range(1, 11): 
    valor = i * numero
    print(f'{i} X {numero} = {valor}')