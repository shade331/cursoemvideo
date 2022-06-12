tupla = ('Corinthians', 'Palmeiras', 'Santos',
         'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=-'*15)
print(f'Lista de times do brasileirão: {tupla}')
print('-=-'*15)
print(f'Os 5 primeiros são: {tupla[0:5]}')
print('-=-'*15)
print(f'Os 4 últimos são: {tupla[16:21]}')
print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(tupla)}')
print('-=-'*15)
print(f'O Chapecoense está na {tupla.index("Chapecoense") + 1}ª posição')
