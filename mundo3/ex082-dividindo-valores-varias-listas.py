c = []
p = []
i = []
while True:
    n = int(input('Digite um número: '))
    c.append(n)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('-='*30)
print(f'A lista completa é {c}')
for n in c:
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
print(f'A lista de pares é {p}')
print(f'A lista de ímpares é {i}')
