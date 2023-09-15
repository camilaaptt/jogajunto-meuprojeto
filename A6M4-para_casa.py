'''
EM SQUADS

Leiam o texto abaixo e resolvam.

Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.

1. Solicitação de Entrada:
    - Implementem a solicitação de entrada de uma palavra (string).

2. Contagem de Vogais:
    - Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
    - Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
    - Imprima o número total de vogais na palavra.
'''

palavra = input("Digite uma palavra: ")

palavra = palavra.lower()

totalVogais = 0

vogais = ['a', 'e', 'i', 'o', 'u']

for caractere in palavra:
    
    if caractere in vogais:
        totalVogais += 1

print(f"O total de vogais na palavra '{palavra}' é: {totalVogais}")

