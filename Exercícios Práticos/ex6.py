import math

def main():
    print("===CALCULADORA DE IMC===")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (math.pow(altura, 2))

    print(f'Seu IMC = {imc:.2f}')

main()