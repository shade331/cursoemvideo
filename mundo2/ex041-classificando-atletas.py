from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento: '))
i = atual - a
print(f'O atleta tem {i} anos.')
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classificação: JUNIOR')
elif i <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
