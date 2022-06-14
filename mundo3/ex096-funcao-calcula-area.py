def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m²')


# Programa principal
print('Controle de Terrenos')
print('-'*20)
lar = float(input('LARGURA (M): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)
