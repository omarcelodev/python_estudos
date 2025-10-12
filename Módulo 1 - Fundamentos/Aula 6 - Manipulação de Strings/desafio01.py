def inversor_texto():
    while True:
        frase_original = input("Digite uma frase: ")

        frase_limpa = frase_original.lower()
        frase_limpa = frase_limpa.replace(" ", "")

        frase_invertida_exibicao = frase_original[::-1]

        frase_invertida = frase_limpa[::-1]

        print("Frase original:", frase_original)
        print("Frase Invertida:", frase_invertida_exibicao)

        if frase_limpa == frase_invertida:
            print("A frase é um palindromo")
        else:
            print("A frase não é um palindromo")

        if input("Deseja inverter outra frase? (s/n): ").lower() == 'n':
            break
inversor_texto()