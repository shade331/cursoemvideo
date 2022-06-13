a = {}
a['nome'] = str(input('Nome: '))
a['média'] = float(input(f'Média de {a["nome"]}: '))
if a['média'] >= 7:
    a['situação'] = 'Aprovado'
elif 5 <= a['média'] < 7:
    a['situação'] = 'Recuperação'
else:
    a['situação'] = 'Reprovado'
print('-='*30)
for k, v in a.items():
    print(f' - {k} é igual a {v}')
