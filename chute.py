from ast import While
from random import randrange, uniform

num = randrange(1, 7)
x = 0
while x != num:
    x = int(input('Adivinhe o valor que estou pensando(entre 1 e 6): '))
    if x > 6 or x < 0:
        print('Digite um valor entre 1 e 6')

print('Você conseguiu!')
