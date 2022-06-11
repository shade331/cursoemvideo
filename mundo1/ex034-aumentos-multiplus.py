s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250:
    a = s * 1.15
else:
    a = s * 1.10
print(f'Quem ganhava R${s:.2f} passa a ganhar R${a:.2f} agora.')
