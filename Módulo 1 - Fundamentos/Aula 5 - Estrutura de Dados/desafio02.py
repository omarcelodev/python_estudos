def numeros():
    lista_numeros = []

    for i in range(10):
        numeros = int(input(f"Digite o {i + 1}° numero:"))
        lista_numeros.append(numeros)
    
    print("Números digitados:", lista_numeros)

    total = soma(lista_numeros)

    print("Maior Número:", max(lista_numeros))
    print("Menor Número:", min(lista_numeros))
    print("Média:", total / 10)


def soma(lista_numeros):
    soma_total = 0

    for i in lista_numeros:
        soma_total += i
    
    return soma_total

numeros()