#Variáveis Global
x = 'Global'

def imprimir():
    print(f'{x} na função imprimir()')

imprimir()
print('f{x} fora da função')

x = 3

def  add():
    global x
    x = x + 5
    print(x)

add()