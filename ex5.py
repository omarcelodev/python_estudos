#Números

a = 15 #<class 'int'>
b = 4.75 #<class 'float'>
c = 5j #<class 'complex'>

print(type(a))
print(type(b))
print(type(c))

#Constantes
import cmath

print(f'Valor de PI: {cmath.pi}')
print(f'Valor de e: {cmath.e}')

#Gerando números Aleatorios
import random
x = random.randrange(1,100)
print(x)

#Conversão de números (casting)
x = 15
y = 4.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

print(float(x))
print(int(y))

print(complex(x))
