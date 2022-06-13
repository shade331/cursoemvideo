ficha = []
while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1+n2)/2
    ficha.append([n, [n1, n2], m])
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*35)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    o = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if o == 999:
        print('Finalizando...')
        break
    if o <= len(ficha) - 1:
        print(f'Notas de {ficha[o][0]} são {ficha[o][1]}')
print('<<< VOLTE SEMPRE >>>')
