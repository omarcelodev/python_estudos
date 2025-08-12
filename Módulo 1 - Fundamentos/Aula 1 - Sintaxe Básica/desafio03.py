num1 = input("Digite o primeiro número: ")
num1 = int(num1)

num2 = input("Digite o segundo número: ")
num2 = int(num2)

if num1 > num2:
    print("O", num1, "é maior que o",num2)
elif num1 < num2:
    print("O" ,num1, "é menor que o", num2)
else:
     print("O", num1, "é igual ao",num2)

if num1 % num2 == 0:
    print("Ambos são multiplos um do outro")
else: 
    print("Não são multiplos")