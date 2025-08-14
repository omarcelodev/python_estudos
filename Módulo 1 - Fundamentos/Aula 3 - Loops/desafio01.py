for i in range(3):
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    
    if usuario == 'admin' and senha == '1234':
        print("Acesso Liberado")
        break
    else:
        print("Acesso Negado")

if usuario != 'admin' and senha != '1234':
    print("Número máximo de tentativas atingidas")

 