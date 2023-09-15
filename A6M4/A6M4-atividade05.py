'''
ATIVIDADE:

EM SQUADS

Leiam o texto abaixo e resolvam.

O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. 

Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário tem o 

@jogajuntoinstituto.org no texto. 

Crie um input para verificar esse texto.

Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. Execute os testes, 

documente e suba os resultados no Bitrix da sua equipe. 
'''

email_check = False
dominio = "jogajuntoinstituto.org"

while email_check == False:
    email = input("Digite o seu email: ")

    if dominio in email:
        print("Este é um email joga junto")
        email_check = True
    else:
        print("Este não é um email do instituto")

