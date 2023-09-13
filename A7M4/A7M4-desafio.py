import os

dados = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

pasta_destino = "pasta_dados"

if not os.path.exists(pasta_destino):
    os.mkdir(pasta_destino)
    print(f"Pasta '{pasta_destino}' criada com sucesso!")

caminho_arquivo = os.path.join(pasta_destino, "dados.txt")

with open(caminho_arquivo, "w") as arquivo:
    for item in dados:
        arquivo.write(item + "\n")

print(f"Dados salvos com sucesso em '{caminho_arquivo}'!")


