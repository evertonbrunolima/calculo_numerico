#erro = float(input ('digite o erro: '))
#erro_dif = erro
#maximo_interações = int(input ('digite o maximo de interações: '))
#chute = float(input ('digite o teste inicial: '))
erro = 0.001
erro_dif = erro
maximo_interações =1000
chute = 0
matriz_indices = [[3,1,-5],[4,-1,1],[1,2,-1]]
matriz_resultado = [10,7,15]
valores_calculos = [chute,chute,chute]
valores_anteriores = [0,0,0]
matriz_variaveis = ['X','Y','Z']


def maior_numero(matriz): 
    vetor_resultado = []

    for indicex, x in enumerate(matriz): 
        for indicey, y in enumerate(x):
            if (indicey == 0): 
                maior = indicey
            elif (modulo(x[maior])<modulo(y)):
                maior = indicey
        vetor_resultado.append(maior) 
    print ("vetor dos maiores") 
    print (vetor_resultado)
    return vetor_resultado
    

def verifica_matriz(matriz): 
    matriz_resultado = []
    for indicex, x in enumerate(matriz): 
        for indicey, y in enumerate(x):
            if (indicex == indicey): 
                elemento_da_linha = y
                soma_elementos = 0
                for elemento in x: 
                    if (elemento_da_linha != elemento):
                            soma_elementos+=modulo(elemento)
                if (modulo(elemento_da_linha) >= soma_elementos): 
                    matriz_resultado.append(1)
                else: 
                    matriz_resultado.append(0)

    print (matriz_resultado)
    return matriz_resultado


def organiza_matriz(matriz, matriz_resultado):
    maior_elemento_linha = maior_numero(matriz)
    for indicex, x in enumerate(maior_elemento_linha): 
        for indicey, y in enumerate(maior_elemento_linha): 
            if (x>y):
                auxiliar_matriz = matriz[x]
                matriz[x] = matriz[y]
                matriz[y] = auxiliar_matriz
                auxiliar_resultado = matriz_resultado[x]
                matriz_resultado[x] = matriz_resultado[y]
                matriz_resultado[y] = auxiliar_resultado
                auxiliar = y
                y = x
                x = auxiliar
    maior_elemento_linha = maior_numero(matriz)            
    checkagem = verifica_matriz(matriz)
    for i in checkagem:
         if (i == 0): 
            return False, matriz, matriz_resultado  
    return True, matriz, matriz_resultado


def calcula_matriz(matriz,matriz_resultado, valores_calculados,tam_matriz,erro):
    matriz_da_multiplicacao = []
    for i in range (tam_matriz): 
        matriz_da_multiplicacao.append(matriz[i][0]*valores_calculados[0]+matriz[i][1]*valores_calculados[1]+matriz[i][2]*valores_calculados[2]) 

    
    for indicei, i in enumerate(matriz_da_multiplicacao):
        resultado =  modulo(i-matriz_resultado[indicei])
        if (resultado<erro):
            result = True
        else: 
            return False
    return result

def modulo(valor): 
    if (valor<0): 
        return  -valor
    else: 
       return  valor
        

        
print('\n______________________________\n')
organizacao, matriz_indices,matriz_resultado = organiza_matriz(matriz_indices, matriz_resultado)
print(matriz_indices)
print(matriz_resultado)
if (organizacao): 
    print('A matriz foi organizada!')
else: 
    print('Matriz não possui organização possivel')
print('\n______________________________\nComeçando os calculos: \n')


for x in range(0,maximo_interações):
    for indice, valor in enumerate(valores_calculos): 
        valores_anteriores[indice] = valor

    #calculo do X
    valores_calculos[0] = (matriz_resultado[0]-matriz_indices[0][1]*valores_anteriores[1]-matriz_indices[0]
    [2]*valores_anteriores[2])/matriz_indices[0][0]

    #calculo do Y
    valores_calculos[1] = (matriz_resultado[1]-matriz_indices[1][0]*valores_anteriores[0]-matriz_indices[1][2]*valores_anteriores[2])/matriz_indices[1][1]

    #calculo do Z
    valores_calculos[2] = (matriz_resultado[2]-matriz_indices[2][1]*valores_anteriores[1]-matriz_indices[2][1]*valores_anteriores[0])/matriz_indices[2][2]
    print(f'calculo {x}: x= {valores_calculos[0] } | y={valores_calculos[1]  } | z={valores_calculos[2]}')


    diferenca = []

    for indice, i in enumerate(valores_calculos):
        diferenca.append(modulo(i - valores_anteriores[indice]))
    
    teste = True
    for i in diferenca: 
        if (i>erro_dif): 
            teste = False


    if (teste): 
        if(calcula_matriz(matriz_indices,matriz_resultado,valores_calculos,3,erro)): 
            print ("resultado encontrado!")
            break
        else: 
            erro_dif = erro_dif/100
       






