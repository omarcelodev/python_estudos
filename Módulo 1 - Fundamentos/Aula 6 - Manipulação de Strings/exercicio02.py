def nome_completo():
    while True:
        nome = input("Digite seu nome completo: ")
    
        print("Nome Maiúsculo:", nome.upper())

        nome_sem_espaco = len(nome.replace(" ", ""))
        print(f"Seu nome tem {nome_sem_espaco} letras")

        primerio_nome = nome.split()[0]
        print("Seu primeiro nóme é:", primerio_nome)

        if input("Deseja escrever outro nome? (s/n): ") == 'n':
            break

nome_completo()