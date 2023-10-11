pontos = [
            [8,9], 
            [10,5],
            [6,5],
            [10,25]
        ]

A = []
X = []
B = []

for indice,ponto in enumerate(pontos): 
    linha = []
    for i in range(len(pontos)-1, -1, -1): 
        linha.append(ponto[0]**i)
    A.append(linha)
    X.append(f'X{indice}')
    B.append(ponto[0])

print('Matriz A:')
for linha in A: 
    print(f'{linha}')

print('\nMatriz X:')
for x in X: 
    print(f'{x}')

print('\nMatriz B:')
for b in B: 
    print(f'{b}')

