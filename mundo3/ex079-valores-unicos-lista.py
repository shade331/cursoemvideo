listanum = []
while True:
    v = int(input(f'Digite um valor: '))
    if v not in listanum:
        listanum.append(v)
        print('Valor adicionado com sucesso...')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'N':
            break
    else:
        print('Valor duplicado! Não vou adicionar...')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'N':
            break
print('-='*40)
listanum.sort()
print(f'Você digitou os valores {listanum}')
