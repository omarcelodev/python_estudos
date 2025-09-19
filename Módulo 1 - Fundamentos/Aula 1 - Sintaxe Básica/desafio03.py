num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O {num1} é maior que o {num2}")
elif num1 < num2:
     print(f"O {num1} é menor que o {num2}")
else:
      print(f"O {num1} é igual ao {num2}")

if num1 % num2 == 0 or num2 % num1 == 0:
    print("Ambos são multiplos um do outro")
else: 
    print("Não são multiplos")