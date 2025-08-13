lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("O triangulo é escaleno")
else:
    print("O triângulo é isoceles")
