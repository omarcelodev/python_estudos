num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operacao = input("Digite a operação: ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    if num2 == 0:
        print("Divisão Inválida")
    else:
        print(num1 / num2)
else:
    print("Operação Inválida")