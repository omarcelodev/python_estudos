agenda = {
    "Marcelo": "62999448879",

    "Ana Luísa": "62995647943"
}

def renomear(nome):
    nomenovo = input("Digite o novo nome do contato: ")

    telefone = agenda[nome]

    agenda[nomenovo] = telefone

    del agenda[nome]

    print("Contato renomeado com sucesso")
    print(agenda)

def adicionar():

    print("===Adição de Contato===")

    while True:
        nome = input("Digite o nome do contato: ")
        if nome in agenda:
            print("Já existe um contato com esse nome! Deseja renomealo?")
            while True:
                opcao = int(input("Digite 1 para sim e 0 para não: "))
                if opcao == 1:
                    renomear(nome)
                    return
                elif opcao == 0:
                    break
                else:
                    print("Opção Inválida!")
            continue

        else:
            while True:
                telefone = input("Digite o telefone do contato: ")
                if telefone in agenda.values():
                    print("Esse telefone já está cadastrado")
                else:
                    agenda[nome] = telefone
                    print("Contato cadastrado com sucesso!")
                    break
            break

def buscar():
    print("===Buscar Contatos===")

    while True:
        nome = input("Digite o nome do contato: ")

        if nome in agenda:
            print("Telefone: ", agenda[nome])
            break
        else:
            print("Não existe nenhum contato com esse nome!")

def remover():
    print("===Remover Contato===")

    while True:
        nome = input("Digite o nome do contato que deseja remover: ")

        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido com sucesso!")
            return
    
        else:
            print("Esse contato não está adicionado a sua lista! Deseja Adicionalo?")
            while True:
                opcao = int(input("Digite 1 para sim e 0 para não: "))
                if opcao == 1:
                    adicionar()
                    return
                elif opcao == 0:
                    break
                else:           
                    print("Opção Inválida!")

def menu():
    print("===AGENDA DE CONTATOS===\n")

    print(agenda)

    while True:
        print("\nSelecione uma opção:")
        print("1) Adcionar Contatos")
        print("2) Remover Contatos")
        print("3) Buscar Contatos")
        print("4) Encerrar Programa")
        opcao = int(input("Sua opção: "))

        if opcao == 1:
            adicionar()
        elif opcao == 2:
            remover()
        elif opcao == 3:
            buscar()
        elif opcao == 4:
            break
        else:
            print("Opção Inválida, tente novamente!")
            
menu()