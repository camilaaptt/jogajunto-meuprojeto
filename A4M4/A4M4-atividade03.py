'''
Mini Case 3: Operações de teste

Imagine que você está em um processo se seleção para ocupar uma vaga de QA e, para testarem seus conhecimentos sobre OPERADORES, propõem o seguinte:

Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:

primeiro output: deve apresentar como resultado o dobro do valor inserido;
segundo output: deve apresentar como resultado o triplo do valor inserido;
terceiro output: deve apresentar como resultado o valor inserido ao quadrado;
quarto output: deve apresentar como resultado a raiz quadrada do valor inserido;
quinto output: deve apresentar como resultado a raíz cúbica do valor inserido.

'''

valor = float(input('Insira o valor desejado: '))

calc1 = valor * 2
calc2 = valor * 3
calc3 = valor ** 2
calc4 = valor ** (1/2)
calc5 = valor ** (1/3)

print(f"O dobro do valor inserido é: {calc1}.")
print(f"O triplo do valor inserido é: {calc2}.")
print(f"O valor inserido ao quadrado é: {calc3}.")
print(f"A raiz quadrada do valor inserido é: {calc4}.")
print(f"A raiz cúbica do valor inserido é: {calc5}.")