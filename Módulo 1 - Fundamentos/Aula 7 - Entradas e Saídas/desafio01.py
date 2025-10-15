def pedir_numero():
    numero = float(input("Digite o número: "))

    return numero

def calculadora(opcao):
    if opcao == 1:
        #soma
        numero_1 = pedir_numero()
        numero_2 = pedir_numero()

        soma = numero_1 + numero_2

        print(f"{numero_1:.2f} + {numero_2:.2f} = {soma:.2f}")
    
    if opcao == 2:
        #subtração
        numero_1 = pedir_numero()
        numero_2 = pedir_numero()

        subtracao = numero_1 - numero_2

        print(f"{numero_1:.2f} - {numero_2:.2f} = {subtracao:.2f}")

    if opcao == 3:
        #multiplicação
        numero_1 = pedir_numero()
        numero_2 = pedir_numero()

        multiplicacao = numero_1 * numero_2

        print(f"{numero_1:.2f} * {numero_2:.2f} = {multiplicacao:.2f}")

    if opcao == 4:
        #divisão
        while True:
            numero_1 = pedir_numero()
            numero_2 = pedir_numero()

            if numero_2 == 0:
                print("Não se pode dividir por 0! Tente novamente.")
            else:
                break

        divisao = numero_1 / numero_2

        print(f"{numero_1:.2f} / {numero_2:.2f} = {divisao:.2f}")

def menu():
    while True:
        print("=== CALCULADORA SIMPLES ===")
    
        print("Digite a operação que deseja realizar.")
        print("(1) Soma")
        print("(2) Subtração")
        print("(3) Multiplicação")
        print("(4) Divisão")
        print("(0) Encerrar Programa")
        opcao = int(input("Sua Opção: "))

        if opcao in [1, 2, 3, 4]:
            calculadora(opcao)
        elif opcao == 0:
            print("Programa Encerrado...")
            break
        else:
            print("Opção Inválida. Tente Novamente!")

menu()