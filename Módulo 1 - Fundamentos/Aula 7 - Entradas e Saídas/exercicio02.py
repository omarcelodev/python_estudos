numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

print(f"Soma: {numero_1} + {numero_2} = {numero_1 + numero_2}")
print(f"Diferença: {numero_1} - {numero_2} = {numero_1 - numero_2}")
print(f"Produto: {numero_1} x {numero_2} = {numero_1 * numero_2}")

if numero_2 == 0:
    print("Quociente: Não é possível dividir por 0!")
else:
    print(f"Quociente: {numero_1} / {numero_2} = {numero_1 / numero_2:.2f}")