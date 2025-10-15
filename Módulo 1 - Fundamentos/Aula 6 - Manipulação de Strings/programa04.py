#Testando contéudo da string
#Retorna true ou false dependendo do contéudo

def true_or_false(teste):
    if teste:
        print("True")
    else:
        print("False")

texto = input("Frase: ")

teste = texto.isalpha() #True se so tem letras
true_or_false(teste)

teste = texto.isdigit() #True se so tem numeros
true_or_false(teste)

teste = texto.isalnum() #True se tem letras e/ou numeros
true_or_false(teste)

teste = texto.startswith("Py") #True se começa com "Py"
true_or_false(teste)

teste = texto.endswith("on") #True se termina com "on"
true_or_false(teste)

