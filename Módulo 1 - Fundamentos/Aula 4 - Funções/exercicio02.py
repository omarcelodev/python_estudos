def area_retangulo(base, altura):
    return (base * altura) / 2

base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))

area = area_retangulo(base, altura)

print("O valor da área é:", area)