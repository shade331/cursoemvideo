print(f'{"LOJAS SHADEZORD":=^40}')
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual é a opção? '))
if o == 1:
    print(f'Sua compra de R${p:.2f} vai custar R${p*0.90:.2f} no final.')
elif o == 2:
    print(f'Sua compra de R${p:.2f} vai custar R${p*0.95:.2f} no final.')
elif o == 3:
    print(f'Sua compra será parcelada em 2x de R${p / 2:.2f}')
    print(f'Sua compra de R${p:.2f} vai custar R${p:.2f} no final.')
elif o == 4:
    tp = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {tp}x de R${p*1.20 / tp:.2f} COM JUROS')
    print(f'Sua compra de R${p:.2f} vai custar R${p*1.20:.2f} no final.')
else:
    print('Opção inválida. Tente novamente.')
