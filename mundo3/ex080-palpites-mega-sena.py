from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
q = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
c = 0
while tot <= q:
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    c = 0
print('-='*3, f' SORTEANDO {q} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '<BOA SORTE>', '-='*5)
