def inversor_texto():
    frase_original = input("Digite uma frase: ")

    frase_limpa = frase_original.lower()
    frase_limpa = frase_limpa.replace(" ", "")

    frase_invertida = frase_limpa[::-1]

    print("Frase original:", frase_original)
    print("Frase Invertida:", frase_invertida)

    if frase_limpa == frase_invertida:
        print("A frase é um palindromo")
    else:
        print("A frase não é um palindromo")

inversor_texto()