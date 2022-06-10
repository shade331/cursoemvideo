si = 0
mi = 0
mih = 0
nv = ''
tm20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    si += i
    if p == 1 and s in 'Mm':
        mih = i
        nv = n
    if s in 'Mm' and i > mih:
        mih = i
        nv = n
    if s in 'Ff' and i < 20:
        tm20 += 1
mi = si / 4
print(f'A média de idade do grupo é de {mi} anos')
print(f'O homem mais velho tem {mih} anos e se chama {nv}')
print(f'Ao todo são {tm20} mulheres com menos de 20 anos')
