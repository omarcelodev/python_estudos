nomes = []

for i in range(5):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)

for nome in nomes:
    print("Bem vindo(a)!", nome)