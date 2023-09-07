'''
EM SQUADS

Leiam o texto abaixo e resolvam.

Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês 
de aulas gratuitas para presentear um acompanhante. Caso contrário, ele não se qualifica para
o benefício.

Na catraca de acesso, haverá uma tela voltada para o cliente. 
Todos os dias, quando ele passar, deve aparecer a mensagem 
"VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

Quando ele completar 21 identificações seguidas, deve aparecer a mensagem 
"UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".

Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, 
deve aparecer "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM 
DE 21 DIAS PARA A PROMO TREINA JUNTO."
'''

frequencia = int(input('Digite a sua frequência: '))
faltas = int(input('Digite a sua quantidade de faltas: '))

if frequencia < 21 and faltas == 0:
    print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
elif frequencia == 21 and faltas == 0:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
else:
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
