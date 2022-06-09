i = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
b = int(input('Sua opção: '))
if b == 1:
    print(f'{i} convertido para BINÁRIO é igual a {bin(i)[2:]}')
elif b == 2:
    print(f'{i} convertido para OCTAL é igual a {oct(i)[2:]}')
elif b == 3:
    print(f'{i} convertido para HEXADECIMAL é igual a {hex(i)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
