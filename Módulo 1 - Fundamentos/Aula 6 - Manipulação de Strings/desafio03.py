def decodificador():
    frase = input("Digite uma frase:").lower()

    frase_codificada = ""
    simbolo = "*"
    
    for letra in frase:
        if letra in "aeiou":
            frase_codificada += simbolo
        else:
            frase_codificada += letra

    print(frase_codificada)



decodificador()