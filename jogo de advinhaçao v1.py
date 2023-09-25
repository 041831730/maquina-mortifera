from random import randint
from time import sleep #o computador pausa por segundos
computador = randint(0, 5) #faz o computador pensar
print('-=- ' * 10)
print('eu pensei em um numero de 0 a 5...')
print('-=- ' * 10)
jogador = int(input('em que numero pensei? ')) #interage com o jogador
print('LOADING...' * 3)
sleep(3)
if jogador == computador :
    print('+ RESPECT')
else :
    print('GAME OVER')
print('o computador pensou no numero {}'.format(computador))