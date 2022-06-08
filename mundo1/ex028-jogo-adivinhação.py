from random import randint
from time import sleep
c = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
j = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if c == j:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {c} e não no {j}!')
