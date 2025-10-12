def analisador_palavras():
    while True:
        frase = input("Digite uma frase:")

        palavras = frase.split()

        tamanho_max = len(max(palavras, key=len))
        maiores = [p for p in palavras if len(p) == tamanho_max]

        print(f"A frase tem {len(palavras)} palavras")
        print(f"A primeira palavra é:{palavras[0]}")
        print(f"A última palavra é:{palavras[-1]}")
        print(f"A(s) maior(es) palavra(s) é/são: {', '.join(maiores)}")

        if input("Deseja inserir outra frase? (s/n): ").lower() == 'n':
            break

analisador_palavras()