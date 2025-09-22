agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"Contato{nome} adicionado com sucesso!")

def buscar_contato(nome):
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

adicionar_contato("Marcelo", "62999448879")
adicionar_contato("Ana", "4444444")

buscar_contato("Marcelo")
remover_contato("Ana")
buscar_contato("Ana")

print("Agenda:", agenda)

