#erro = float(input ('digite o erro: '))
#erro_dif = erro
#maximo_interações = int(input ('digite o maximo de interações: '))
#chute = float(input ('digite o teste inicial: '))
#erro = 0.001
#erro_dif = erro
#maximo_interações =100
#chute = 0
#matriz_indices = [[3,1,-5],[4,-1,1],[1,2,-1]]
#matriz_resultado = [10,7,15]
#valores_calculos = [chute,chute,chute]
#valores_anteriores = [0,0,0]
#matriz_variaveis = ['X','Y','Z']


#metodo de execução
def f(x):
   return x**2-16
  
def metodo_exec(): 
    print ('----------------------------------------------------')
    print ('\tMetodo Execução')
    print ('----------------------------------------------------')
    while (True): 
        n1 = float(input('digite o primeiro numero do intervalo: '))
        n2 = float(input('digite o segundo numero do intervalo: '))
        if (f(n1)*f(n2) < 0): 
            break 
        else:
            print('dados errados!')
    erro = float(input('digite o numero do erro: '))
    escape = int(input('digite o numero maximo de tentativa: '))
        
    for i in range (escape):
        media = (n1+n2)/2 
        if (modulo(f(media)) < erro): 
            break
        if (f(n1)*f(media)<0): 
            n2 = media;  
        else: 
            n1 = media; 
        print(f' O valor encontrado foi: {media}')
        print(f"calculo{i} - media={media}")


#metodo secante
def metodo_secante(): 
    print ('----------------------------------------------------')
    print ('\tMetodo Secante')
    print ('----------------------------------------------------')
    n1 = int (input('digite o primeiro numero: '))
    n2 = int (input('digite o segundo numero: '))
    erro = float (input('digite o erro: '))
    maximo = int (input('digite o maximo de interações: '))
    cont = 0

    def angulo(x1,x2): 
        return (f(x1)-f(x2))/(x1-x2)

    def eraiz(x):
        if ( -erro < f(x) and f(x) < erro): 
            print ('o numero ' + str(x) + ' é raiz')
            return 1
        else: 
            return 0

    def compara_raiz_maior (x,x1):
        resultado_fx = f(x)
        resultado_fx1= f(x1)
        if (resultado_fx <0):
            resultado_fx = - resultado_fx
        if (resultado_fx1 <0):
            resultado_fx1 = - resultado_fx1

        return  resultado_fx>resultado_fx1
        
    while (cont< maximo): 
        if (eraiz(n1) or eraiz(n2)): 
            break
        raiz_sec = -f(n1)*(1/angulo(n1,n2))+n1
        
        if (eraiz(raiz_sec)):
            break
        if (compara_raiz_maior(raiz_sec,n1)): 
            print ('a raiz da secante não se aproximada da raiz da equacao')
            break
        n1 = raiz_sec

        cont+=1

#Newton
def metodo_newton():
    print ('----------------------------------------------------')
    print ('\tMetodo Newton')
    print ('----------------------------------------------------')
    n1 = float(input("Digite um numero: "))
    erro = float (input('Digite o erro: '))
    maximo = int (input('Digite o maximo de interações: '))
    funcao = "x**2-16"
    #n1 = 10
    #erro = 0.0001
    #maximo = 1000



    def f_derivada(x): 
        tendencia= 0.0000001
        return (f(tendencia+x)-f(x))/tendencia
    
    def eh_raiz(x):
        return modulo(f(x)) < erro
    
    def compara(proximo, anterior):
        if (proximo < 0): 
            proximo = -1*proximo
        
        if (anterior < 0):
            anterior = -1*anterior
        
        return f(anterior)<f(proximo)
        

    for i in range (maximo): 
        anterior = n1
        if (compara(n1,anterior)):
            print (f""" A função esta se afastado: """)
            break
        
        if (eh_raiz(n1)): 
            print (f"""A raiz da funcao {funcao} é: {n1} \n f({n1}) = {f(n1)} \nnumero de interações: {i}
                """)
            break
        n1 = anterior-f(anterior)/f_derivada(anterior)
        print(f"calculo{i} - n1={n1}")

    
    

#gauss_Jacobi
def maior_numero(matriz): 
    print ('----------------------------------------------------')
    print ('\tMetodo Gauss-Jacobi')
    print ('----------------------------------------------------')
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
        


def metodo_gauss():   

    erro = float(input ('digite o erro: '))
    erro_dif = erro
    maximo_interações = int(input ('digite o maximo de interações: '))
    chute = float(input ('digite o teste inicial: ')) 
    matriz_indices = [[3,1,-5],[4,-1,1],[1,2,-1]]
    matriz_resultado = [10,7,15]
    valores_calculos = [chute,chute,chute]
    valores_anteriores = [0,0,0] 


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

        for indicez, z in enumerate(matriz_indices):
            soma = 0
            for indicey, y in enumerate(z): 
                if (indicez == indicey): 
                    div = y
                else: 
                    soma += y*valores_anteriores[indicey]
            valores_calculos[indicez] = (matriz_resultado[indicez]-soma)/div
        print(f'calculo {x}: x= {valores_calculos[0]} | y={valores_calculos[1]  } | z={valores_calculos[2]}')
        


        #calculo do X
        #valores_calculos[0] = (matriz_resultado[0]-matriz_indices[0][1]*valores_anteriores[1]-matriz_indices[0]
        #[2]*valores_anteriores[2])/matriz_indices[0][0]

        #calculo do Y
        #valores_calculos[1] = (matriz_resultado[1]-matriz_indices[1][0]*valores_anteriores[0]-matriz_indices[1][2]*valores_anteriores[2])/matriz_indices[1][1]

        #calculo do Z
        #valores_calculos[2] = (matriz_resultado[2]-matriz_indices[2][0]*valores_anteriores[0]-matriz_indices[2][1]*valores_anteriores[1])/matriz_indices[2][2]
        #print (f" ({matriz_resultado[2]}-{matriz_indices[2][0]}*{valores_anteriores[0]}-{matriz_indices[2][1]}*{valores_anteriores[1]})/{matriz_indices[2][2]}")
        #print(f'calculo {x}: x= {valores_calculos[0]} | y={valores_calculos[1]  } | z={valores_calculos[2]}')


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
       


def main():
    while (True):
        print ('\n----------------------------------------------------')
        print ('\tMenu')
        print ('----------------------------------------------------')
        metodo = int(input(f"""\nDigite o numero do metodo que deseja utilizar:\n   1- execução\n   2- Secante\n   3- Newton\n   4- Gauss-Jacobi\n   0- sair         
            """))
        if (metodo == 1):
            metodo_exec()
        elif (metodo == 2): 
            metodo_secante()
        elif (metodo == 3): 
            metodo_newton()
        elif (metodo == 4): 
            metodo_gauss()
        elif (metodo == 0): 
            break
        else: 
            print ('\nopção invalida\n')

    





main()
#metodo_newton()
