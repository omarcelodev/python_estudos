capitais_brasileiras = [
    "riobranco",      # Acre
    "maceio",        # Alagoas
    "macapa",        # Amapa
    "manaus",        # Amazonas
    "salvador",         # Bahia
    "fortaleza",     # Ceara
    "brasilia",      # Distrito Federal
    "vitoria",       # Espirito Santo
    "goiania",       # Goias
    "saoluis",      # Maranhao
    "cuiaba",        # Mato Grosso
    "campogrande",        # Mato Grosso do Sul
    "belohorizonte",  # Minas Gerais
    "belem",         # Para
    "joaopessoa",   # Paraiba
    "curitiba",      # Parana
    "recife",        # Pernambuco
    "teresina",      # Piaui
    "riodejaneiro",# Rio de Janeiro
    "natal",         # Rio Grande do Norte
    "portoalegre",  # Rio Grande do Sul
    "portovelho",   # Rondonia
    "boavista",     # Roraima
    "florianopolis", # Santa Catarina
    "saopaulo",     # Sao Paulo
    "aracaju",       # Sergipe
    "palmas"         # Tocantins
]
#Se idade for inválida retorna True
def verificar_idade(idade):
    if idade < 1 or idade > 100:
        print("Idade Inválida! Tente novamente.")
        return True
    else:
        return False

#Se a cidade for inálida retorna True
def verificar_cidade(cidade_formatada):
    if cidade_formatada not in capitais_brasileiras:
        print("Essa cidade não está disponível para escolha!")
        return True
    else:
        return False
    

def mensagem():
    while True:
        nome = input("Digite sue nome: ").strip()

        while True:
            idade = int(input("Digite sua idade: "))
            if verificar_idade(idade) == False:
                break
    
        while True:
            cidade = input("Difite o nome da sua cidade: ")
            cidade_formatada = cidade.lower()
            cidade_formatada = cidade_formatada.replace(" ", "")

            if verificar_cidade(cidade_formatada) == False:
                break

        print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}. Seja bem-vindo!")

        if input("Deseja encerrar o programa?(s/n): ").lower() == 's':
            break

mensagem()