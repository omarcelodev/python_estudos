produtos = {
    "Cereal": 5,
    "Arroz": 8,
    "Café": 10
}

def venda():
    print("===CADASTRO DE VENDAS===\n")
    while True:
        nome = input("Produto Vendido: ")

        if nome not in produtos:
            if input("Produto não cadastrado. Deseja adicionar? (s/n): ").lower() == 's':
                print("Função para cadastrar produto") #adicionar depois
            continue

        quantidade = int(input("Quantidade vendida: "))
        estoque_atual = produtos[nome]

        if quantidade > estoque_atual:
            print(f"Estoque Insuficiente! ({estoque_atual} disponiveis).")

            if input("Deseja repor o estoque? (s/n): ").lower() == 's':
                print("Função para Repor estoque") #Adicionar depois
            continue

        produtos[nome] -= quantidade
            
        print(f"Venda realizada! Estoque atual de {nome}: {produtos[nome]}")

        if input("Deseja realizar uma nova venda? (s/n): ").lower() == 'n':
                break

def menu():
    while True:
        print("===CONTROLE DE ESTOQUE===\n")
        print("Selecione a opção desejada:")
        print("(1)Venda de Produto")
        print("(2)Reposição de Produto")
        print("(3)Listamento de Produtos")
        print("(0)Sair")
        opcao = int(input("Sua opção: "))

        if opcao == 1:
            venda()
        elif opcao == 2:
            print("Reposição")
        elif opcao == 3:
            print("Listamento")
        elif opcao == 0:
            break
        else:
            print("Opção Inválida!")

        
menu()