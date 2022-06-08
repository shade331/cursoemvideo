d = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d:.1f}Km.')
if d <= 200:
    print(f'E o preço da sua passagem será de R${d*0.50:.2f}')
else:
    print(f'E o preço da sua passagem será de R${d*0.45:.2f}')
