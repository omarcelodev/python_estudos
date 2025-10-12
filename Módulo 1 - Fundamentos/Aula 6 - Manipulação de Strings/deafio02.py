def analisador_palavras():
    frase = input("Digite uma frase:")

    palavras = frase.split()
    maior = max(palavras, key=len)

    print(f"A frase tem {len(palavras)} palavras")
    print(f"A primeira palavra é:{palavras[0]}")
    print(f"A última palavra é:{palavras[-1]}")
    print(f"A maior palavra é:{maior}")

analisador_palavras()