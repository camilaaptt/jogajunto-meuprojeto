'''
ATIVIDADE: 

PARTE 3

Agora crie um script para com uma lista de frutas, e outra lista com o nome alergias. 

Insira uma fruta da lista de frutas na lista de alergias. 

Depois crie um for para cada item da lista passar por uma verificação em uma estrutura condicional para verificar 

se está essa fruta está contida na lista de alergias. Caso a fruta esteja na lista, imprima na tela o nome dela. 

'''

frutas = ['maça', 'uva', 'melancia']
alergias = ['kiwi', 'melao', 'uva']

for fruta in frutas:
    if fruta in alergias:
        print(f'A {fruta} que você tem alergia está contida na lista')