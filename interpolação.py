pontos = [
            [8,9], 
            [10,5],
            [6,5]
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

for indice,linha in enumerate(A): 
    print(f'{linha}\t{X[indice]} = {B[indice]}')
