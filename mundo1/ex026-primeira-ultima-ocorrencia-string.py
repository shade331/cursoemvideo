f = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {f.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {f.find("A")+1}')
print(f'A última letra A apareceu na posição {f.rfind("A")+1}')
