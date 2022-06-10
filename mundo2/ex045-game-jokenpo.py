from random import randint
from time import sleep
i = ['PEDRA', 'PAPEL', 'TESOURA']
c = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
if j != 0 and j != 1 and j != 2:
    print('JOGADA INVÁLIDA! Tente novamente!!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print(f'Computador jogou {i[c]}')
print(f'Jogador jogou {i[j]}')
print('-='*11)
if c == 0:  # Computador jogou PEDRA
    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('JOGADOR VENCE')
    elif j == 2:
        print('COMPUTADOR VENCE')
elif c == 1:  # Computador jogou PAPEL
    if j == 0:
        print('COMPUTADOR VENCE')
    elif j == 1:
        print('EMPATE')
    elif j == 2:
        print('JOGADOR VENCE')
elif c == 2:  # Computador jogou TESOURA
    if j == 0:
        print('JOGADOR VENCE')
    elif j == 1:
        print('COMPUTADOR VENCE')
    elif j == 2:
        print('EMPATE')
