'''
EM SQUAD

Leiam o case e resolvam a situação.

A Loja do Joga Junto conta mais uma vez com a colaboração do seu squad! Desta vez, surge a necessidade de desenvolver 
um programa que analisa o CEP inserido pelo usuário e determina se ele é elegível para frete grátis. Para realizar essa 
tarefa, foi definida uma política de frete grátis abrangendo todos os estados das regiões Norte e Nordeste do país.  


- Faça um brainstorming com sua equipe sobre o fluxo e requisitos necessários para construção desse programa
- Desenvolva o programa
- Faça casos de teste para este cenário, documente os testes realizados e insira no Bitrix
- Caso seja encontrado algum bug no seu código, documente-o. 
'''
import requests

estados = ['AM','RR','AP','PA','TO','RO','AC','MA','PI','CE','RN','PE','PB','SE','AL','BA']

def varificaCEP(cep):
    if not cep.isdigit() or len(cep) != 8:
        return "O CEP digitado é inválido."

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    estado = data['uf']

    if estado in estados:
        return(f"O CEP digitado é elegível para frete grátis!")
    else:
        return(f"O CEP digitado não é elegível para frete grátis.")
    

cep = input("Digite o seu CEP: ")
resultado = varificaCEP(cep)
print(resultado)