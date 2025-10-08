produtos = {
    "Cereal": 5,
    "Arroz": 8,
    "Café": 10
}

def venda():
    print("===CADASTRO DE VENDAS===\n")
    while True:
        nome = input("Digite o nome do produto vendido: ")

        if nome in produtos:
            quantidade = int(input("Digite a quantidade vendida: "))

            produtos[nome] -= quantidade

            print("produtos:", produtos)
        else:
            while True:
                print("Este produto não está cadastrado")
                opcao = int(input("Deseja cadastra-lo? (1)Sim (0)Não: "))

                if opcao == 1:
                    print("Função Cadastro") #Adicionar depois
                    break
                elif opcao == 0:
                    break
                else:
                    print("Opção Inválida")
            
        



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