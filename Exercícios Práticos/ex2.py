def main():
    numero1 = int(input("\nDigite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    modulo = numero1 % numero2

    print(f'{numero1} + {numero2} = {soma}')
    print(f'{numero1} - {numero2} = {subtracao}')
    print(f'{numero1} x {numero2} = {multiplicacao}')
    print(f'{numero1} / {numero2} = {divisao}')
    print(f'{numero1} % {numero2} = {modulo}')

main()

