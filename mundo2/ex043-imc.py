p = float(input('Qual é seu peso? (Kg) '))
a = float(input('Qual é sua altura? (m) '))
imc = p / (a ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está no PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif 40 < imc:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
