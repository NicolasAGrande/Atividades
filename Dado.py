from ast import While
from random import randrange, uniform

esc = 1

while esc == 1:
    esc = int(input('Deseja jogar o dado?,  digite 1 para sim e 2 para não'))
    if esc == 1:
        print(randrange(1, 7))
    elif esc > 2:
        print('Escolha 1 ou 2')
        esc = 1
    else:
        break

print('Acabou')