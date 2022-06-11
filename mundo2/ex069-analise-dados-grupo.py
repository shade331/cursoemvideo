t18 = 0
th = 0
tm20 = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if i >= 18:
        t18 += 1
    if s == 'M':
        th += 1
    if s == 'F' and i < 20:
        tm20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {t18}')
print(f'Ao todo temos {th} homens cadastrados')
print(f'E temos {tm20} mulheres com menos de 20 anos')
