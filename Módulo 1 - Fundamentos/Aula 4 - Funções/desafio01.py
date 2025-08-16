def calculator(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Não se pode dividir um número por 0!")
        return num1 / num2
    else:
        print("Operação Inválida")
        return False
        


num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
operacao = input("Digite a operação: ")

resultado = calculator(num1, num2, operacao)

if resultado != False:
    print(f"{num1} {operacao} {num2} = {resultado}")


