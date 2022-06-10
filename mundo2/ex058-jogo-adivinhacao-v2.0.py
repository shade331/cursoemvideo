from random import randint
c = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
a = False
p = 0
while not a:
    j = int(input('Qual é seu palpite? '))
    p += 1
    if j == c:
        a = True
    else:
        if j < c:
            print('Mais... Tente mais uma vez.')
        elif j > c:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {p} tentativas. Parabéns!')
