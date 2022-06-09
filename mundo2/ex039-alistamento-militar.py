from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento: '))
i = atual - a
print(f'Quem nasceu em {a} tem {i} anos em {atual}')
if i == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif i < 18:
    print(f'Ainda faltam {18 - i} anos para o alistamento')
    print(f'Seu alistamento será em {atual + (18 - i)}')
else:
    print(f'Você já deveria ter se alistado há {i - 18} anos.')
    print(f'Seu alistamento foi em {atual - (i - 18)}')
