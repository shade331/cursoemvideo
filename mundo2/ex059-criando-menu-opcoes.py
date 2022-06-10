from time import sleep
a1 = int(input('Primeiro valor: '))
a2 = int(input('Segundo valor: '))
o = 0
while o != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    o = int(input('Qual é a sua opção? '))
    if o == 1:
        print(f'A soma entre {a1} + {a2} é {a1 + a2}')
    elif o == 2:
        print(f'O resultado de {a1} x {a2} é {a1 * a2}')
    elif o == 3:
        if a1 > a2:
            m = a1
        else:
            m = a2
        print(f'Entre {a1} e {a2} o maior valor é {m}')
    elif o == 4:
        print('Informe os números novamente:')
        a1 = int(input('Primeiro valor: '))
        a2 = int(input('Segundo valor: '))
    elif o == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida. Tente novamente.')
    print('-=-'*10)
print('Fim do programa! Volte sempre!')
