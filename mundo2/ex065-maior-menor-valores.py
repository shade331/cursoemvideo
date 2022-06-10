r = 'S'
maior = menor = 0
c = 0
total = 0
while r == 'S':
    n = int(input('Digite um número: '))
    if c == 0:
        maior = n
        menor = n
        c += 1
        total += n
    elif n > maior:
        maior = n
        c += 1
        total += n
    elif n < menor:
        menor = n
        c += 1
        total += n
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = total / c
print(f'Você digitou {c} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
