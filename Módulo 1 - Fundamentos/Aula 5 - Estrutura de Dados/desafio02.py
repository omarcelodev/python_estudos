def numeros():
    lista_numeros = []

    for i in range(10):
            numero = int(input(f"Digite {i + 1}° número: "))
            lista_numeros.append(numero)
    
    print(lista_numeros)

    total = soma(lista_numeros)

    print("A soma dos números: ", total)
    print("O maior número: ", max(lista_numeros))
    print("O menor número: ", min(lista_numeros))
    print("A média: ", total / 10)

def soma(lista_numeros):
    soma_total = 0
    for i in lista_numeros:
        soma_total += i
    
    return soma_total

numeros()
