from random import randint
computador = randint(0, 5) #faz o computador pensar
print('-=-' *50)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*50)
jogador = int(input('Em que numero pensei ? '))#jogador tenta adivinhar
if jogador == computador:
    print('PARABENS! voce consegui vencer !')
else:
    print('Ganhei ! eu pensei no numero {} e não no {} !'.format(computador,jogador))
