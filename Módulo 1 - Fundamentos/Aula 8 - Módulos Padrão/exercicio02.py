import random

nomes = []

for i in range(4):
    nome = input("Digite um nome: ").strip()
    nomes.append(nome)

print(random.choice(nomes))

