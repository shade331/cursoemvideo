listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # :^40 é centralizado com 40 espaços
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')  # :.<30 é alinhado a esquerda com 30 espaços preenchidos por '.'
    elif pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')  # :>7.2f é alinhado a direita com 2 casas depois da vírgula
print('-'*40)
