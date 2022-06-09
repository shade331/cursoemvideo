p = float(input('Primeira nota: '))
s = float(input('Segunda nota: '))
m = (p + s) / 2
print(f'Tirando {p:.1f} e {s:.1f}, a média do aluno é {m:.1f}')
if m < 5:
    print('O aluno está REPROVADO.')
elif 5 <= m <= 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print(f'O aluno está APROVADO.')
