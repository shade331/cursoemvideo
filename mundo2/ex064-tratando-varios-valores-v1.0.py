s = 0
n = 0
c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        c += 1
        s += n
    else:
        print(f'Você digitou {c} números e a soma entre eles foi {s}')
