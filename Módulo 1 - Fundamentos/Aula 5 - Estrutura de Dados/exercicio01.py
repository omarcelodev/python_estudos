numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    
print(numeros)
print("Maior número:", max(numeros))
print("Menor número", min(numeros))
