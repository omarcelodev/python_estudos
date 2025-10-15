def palavra():
    while True:
        palavra = input("Digite uma palavra:")
        palavra_formatada = palavra.lower()

        if palavra_formatada.startswith("a"):
            print("A palavra começa com A!")
        else:
            print("A palavra não começa com A!")

        if palavra_formatada.endswith("o"):
            print("A palavra termina com O!")
        else:
            print("A palavra não termina com O!")
    
        print(f"A letra 'E' Apareceu: {palavra_formatada.count('e')} vezes")

        if input("Deseja escrever outra palavra? (s/n): ").lower() == 'n':
            break

palavra()

