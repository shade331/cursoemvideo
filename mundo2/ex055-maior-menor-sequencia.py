maior = 0
menor = 0
for c in range(1, 6):
    p = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = p
        menor = p
    elif p > maior:
        maior = p
    elif p < menor:
        menor = p
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
