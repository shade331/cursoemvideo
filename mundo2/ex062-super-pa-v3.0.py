print('Gerador de PA')
print('-=-'*10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
total = 0
m = 10
while m != 0:
    total += + m
    while c <= total:
        print(f'{t} → ', end='')
        t += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
