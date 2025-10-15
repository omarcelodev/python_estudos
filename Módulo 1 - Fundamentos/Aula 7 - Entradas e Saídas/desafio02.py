def pedir_numero():
    numero = float(input("Digite a temperatura: "))
    return numero

def conversor_temperatura(opcao):
    if opcao == 1:
        #Fahrenheit -> Celsius
        fahrenheit = pedir_numero()
        celsius = 5 / 9 * (fahrenheit - 32)

        print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")

    elif opcao == 2:
        #Fahrenheit -> Kelvin
        fahrenheit = pedir_numero()
        kelvin = (fahrenheit - 32) * 5 / 9 + 273.15

        print(f"{fahrenheit:.2f}°F = {kelvin:.2f}K")
    
    elif opcao == 3:
        #Celsius -> Fahrenheit
        celsius = pedir_numero()
        fahrenheit = (celsius * 9 / 5) + 32

        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    
    elif opcao == 4:
        #Celsius -> Kelvin
        celsius = pedir_numero()
        kelvin = celsius + 273.15

        print(f"{celsius:.2f}°C = {kelvin:.2f}K")

    elif opcao == 5:
        #Kelvin -> Fahrenheit
        kelvin = pedir_numero()
        fahrenheit = (kelvin - 273.15) * 9/5 + 32

        print(f"{kelvin:.2f}K = {fahrenheit:.2f}°F")

    elif opcao == 6:
        #Kelvin -> Celsius
        kelvin = pedir_numero()
        celsius = kelvin - 273.15

        print(f"{kelvin:.2f}K = {celsius:.2f}°C")

def menu():
    while True:
        print("=== CONVERSOR DE TEMPERTATURA ===")
        print("Selecione o tipo de Conversão")
        print("(1) Fahrenheit -> Celsius")
        print("(2) Fahrenheit -> Kelvin")
        print("(3) Celsius -> Fahrenheit")
        print("(4) Celsius -> Kelvin")
        print("(5) Kelvin -> Fahrenheit")
        print("(6) Kelvin -> Celsius")
        print("(0) Encerrar Programa")
        opcao = int(input("Sua opção: "))

        if opcao in [1, 2, 3, 4, 5, 6]:
            conversor_temperatura(opcao)
        elif opcao == 0:
            print("Programa Encerrado")
            break
        else:
            print("Opção Inválida! Tente novamente.")

menu()