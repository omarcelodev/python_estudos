soma = 0
num = int(input("Digite um número(0 para parar): "))

while num != 0:
    soma += num
    num = int(input("Digite um número(0 para parar): "))

print("Soma total:", soma)
