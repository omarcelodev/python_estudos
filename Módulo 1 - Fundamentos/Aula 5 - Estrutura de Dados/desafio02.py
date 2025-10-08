def numeros():
    lista_numeros = []

    for i in range(10):
            numero = int(input(f"Digite {i + 1}° número: "))
            lista_numeros.append(numero)
    
    print(lista_numeros)
    soma(lista_numeros)
    print("O maior número: ", max(lista_numeros))
    print("O menor número: ", min(lista_numeros))

   


def soma(lista_numeros):
    soma = 0
    for i in lista_numeros:
        soma += i
    
    print("soma dos números: ", soma)


    
numeros()
