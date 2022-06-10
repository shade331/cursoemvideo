from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1, 8):
    n = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - n
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print(f'Ao todo tivemos {tmaior} pessoas maiores de idade')
print(f'E também tivemos {tmenor} pessoas menores de idade')
