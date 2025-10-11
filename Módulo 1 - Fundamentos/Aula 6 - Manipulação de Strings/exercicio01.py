def exercicio():
    while True:
        frase = input("Digite um frase: ")

        print("A frase em maiúsculo: ", frase.upper())
        print("A frase em minúsculo: ", frase.lower())
        print("O tamanho total da frase é: {len(frase)}.")

        if input("Deseja escrever outra frase? (s/n): ") == 'n':
            break

exercicio()