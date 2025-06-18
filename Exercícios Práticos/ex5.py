def main():
    print("===CALCULADORA SIMPLES===")

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação(+ ; - ; * ; /): ")

    if operacao == "+":
        soma = numero1 + numero2
        print(f"{numero1} + {numero2} = {soma}")

    elif operacao == "-":
        subtracao = numero1 - numero2
        print(f"{numero1} - {numero2} = {subtracao}")

    elif operacao == "*":
        multiplicacao = numero1 * numero2
        print(f"{numero1} x {numero2} = {multiplicacao}")

    else:
        divisao = numero1 / numero2
        print(f"{numero1} / {numero2} = {divisao}")

main()