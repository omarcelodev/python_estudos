produtos = {
    "Cereal": 5,
    "Arroz": 8,
    "Café": 10
}

def venda():
    print("\n===CADASTRO DE VENDAS===\n")
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

def reposicao():
    print("\n===CADASTRO DE REPOSIÇÃO===\n")
    
    while True:
        nome = input("Informe o produto que deseja repor: ")
    
        if nome not in produtos:
            if input("Produto não cadastrado. Deseja adicionar? (s/n): ").lower() == 's':
                print("Função para cadastrar produto") # adicionar depois
            continue
        
        while True:
            quantidade = int(input("Informe a quantidade que deseja repor: "))

            if quantidade > 1000:
                print("Valor máximo de estoque ultrapassado")
            elif quantidade < 1:
                print("Valor Inválido!")
            else:
                break
        
        limite = 1000
        produtos[nome] += quantidade

        if produtos[nome] > limite:
            sobra = produtos[nome] - limite
            produtos[nome] = limite
            print(f"Capacidade máxima do estoque atingida. {sobra} unidades não foram adicionadas.")
        else:
            sobra = 0
        
        print(f"Estoque atual de {nome}: {produtos[nome]} unidades.")

        if input("Deseja realizar uma nova reposição? (s/n)").lower() == 'n':
            break

def listagem():
    print("\n===LISTA DE ITENS E QUANTIDADE===\n")

    print(produtos)
    print("\n")


def menu():
    while True:
        print("===CONTROLE DE ESTOQUE===\n")
        print("Selecione a opção desejada:")
        print("(1)Venda de Produto")
        print("(2)Reposição de Produto")
        print("(3)Listamento de Produtos")
        print("(4)Cadastrar item")
        print("(0)Sair")
        opcao = int(input("Sua opção: "))

        if opcao == 1:
            venda()
        elif opcao == 2:
            reposicao()
        elif opcao == 3:
            listagem()
        elif opcao == 4:
            print("Cadastrar")
        elif opcao == 0:
            break
        else:
            print("Opção Inválida!")

        
menu()