from random import randint
v = 0
while True:
    j = int(input('Diga um valor: '))
    c = randint(0, 11)
    total = j + c
    t = ' '
    while t not in 'PpIi':
        t = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {j} e o computador {c}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if t == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif t == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

