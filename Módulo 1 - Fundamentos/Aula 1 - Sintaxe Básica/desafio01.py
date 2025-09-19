from datetime import date

ano_nascimento = int(input("Digite o ano que você nasceu: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")

