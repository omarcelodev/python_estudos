aluno = {
    "nome": "",
    "idade": 0,
    "nota": 0.0
}

aluno["nome"] = input("Nome Aluno: ")
aluno["idade"] = int(input("Idade Aluno: "))
aluno["nota"] = float(input("Nota Aluno: "))

print(aluno)

print("Nota: ", aluno["nota"])