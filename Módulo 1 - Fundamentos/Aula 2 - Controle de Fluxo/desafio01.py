usuario = input("Digite o usuario: ")
senha = int(input("Digite a senha: "))

if usuario == 'admin' and senha == 1234:
    print("Acesso Liberado")
else:
    print("Acesso Negado")