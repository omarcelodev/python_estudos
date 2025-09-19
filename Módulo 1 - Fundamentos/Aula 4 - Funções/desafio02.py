def celsius(temp):
    return (temp - 32) / 1.8

def fahrenheit(temp):
    return temp * 1.8 + 32

print("Escolha o tipo de conversão.")
print("(1) Fahrenheit -> Celsius")
print("(2) Celsius -> Fahrenheit")
opcao = int(input("Sua opção:"))

temp = float(input("Digite a temperatura:"))

if opcao == 1:
    conversao = celsius(temp)
    print(f"A temperatura em celsius é: {conversao:.1f}°C")
elif opcao == 2:
    conversao = fahrenheit(temp)
    print(f"A temperatura em fahrenheit é: {conversao:.1f}°F")
else:
    print("Opcão Inválida!")
