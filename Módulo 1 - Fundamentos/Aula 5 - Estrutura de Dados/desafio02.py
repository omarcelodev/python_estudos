def getnumbers():
    numbers = []

    for i in range(10):
        numbers.append(int(input("Digite um número: ")))

    print(numbers)

def plus(numbers):
    for i in range(10):
        soma += numbers[i]

    print(soma)

getnumbers()
plus(numbers)