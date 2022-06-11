v = 0
while True:
    v = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if v < 0:
        break
    for c in range(1, 11):
        print(f'{v} x {c} = {v * c}')
    print('-'*35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
