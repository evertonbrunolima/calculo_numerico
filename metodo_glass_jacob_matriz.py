import metodo_glass_jaob as m
import copy

def separa_matriz(matriz):
    I = []
    D = []
    S =  []
    for indicel, l in enumerate(matriz): 
        VD = []
        VI = []
        VS = []
        for indicec, e in enumerate(l): 
            if (indicec == indicel): 
                VD.append(e)
                VI.append(0)
                VS.append(0)
            elif indicec<indicel: 
                VD.append(0)
                VI.append(e)
                VS.append(0)
            else:
                VD.append(0)
                VI.append(0)
                VS.append(e)

        I.append(VI)
        D.append(VD)
        S.append(VS)
    return I,S, D


def vet_para_mat(B): 
    try: 
        tamanho_b = len(B[0])
        return B
    except: 
        b_vetor = B 
        B = []
        vetor = True
        for elemento in b_vetor:
            B.append([elemento])
        return B
    
def matriz_para_vet(A):
    if (len(A[0])==1): 
        auxiliar = A
        A = []
        for el in auxiliar: 
            A.append(el[0])
    return A 
    

def mul_matriz(A,B): 
    resultado = []
    B = vet_para_mat(B)
    A = vet_para_mat(A)
    for indiceLA, LA in enumerate (A): 
        resultado_linha = []
        for x in range(len(B[0])):
            mul_elemento = 0
            for indiceE, E in enumerate(LA): 
                mul_elemento += E*B[indiceE][x]  
            resultado_linha.append(mul_elemento)
        resultado.append(resultado_linha)

    resultado = matriz_para_vet(resultado)
            
    return resultado


def soma_matriz(A,B):
    B = vet_para_mat(B)
    A = vet_para_mat(A)
    resultado = []
    for indicelinha , linha in enumerate(A): 
        nova_linha = []
        for indice,elemento in enumerate(linha): 
            nova_linha.append(elemento+B[indicelinha][indice])
        resultado.append(nova_linha)
    resultado = matriz_para_vet(resultado)
    return resultado

def matriz_x_numero(M, A):
    M = vet_para_mat(M)
    resultado = []
    for linha in M: 
        auxiliar_linha = []
        for el in linha:
            auxiliar_linha.append(el*A)
        resultado.append(auxiliar_linha)

    resultado = matriz_para_vet(resultado)
    return resultado

def calcula_determinante(A):
    if len(A[0]) == 1: 
          return A[0]

    if len(A[0]) == 2: 
            return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    if len(A[0]) >= 3: 
        det = 0
        for indice, el in enumerate(A[0]):
            matriz = []
            for indicel, linha in enumerate(A): 
                if indicel != 0: 
                    nova_linha = []
                    for indicem, elm in enumerate(linha): 
                        if indicem != indice: 
                            nova_linha.append(elm)
                    matriz.append(nova_linha)
            #print(matriz)
            det += el*((-1)**(2+indice))*calcula_determinante(matriz)
        return det   
    
def transporta_matriz(matriz): 
    trans = copy.deepcopy(matriz)
    for indicel, linha in enumerate(matriz): 
        for indice, el in enumerate(linha):
            trans[indice][indicel] = el
    return trans

def cria_inversa(matriz): 
    det_matriz = calcula_determinante(matriz)
    inversa = []
    mul = -1
    if len(matriz[0]) == 2: 
        numero = matriz[1][1]
        matriz[1][1] = matriz[0][0] 
        matriz[0][0] = numero
        matriz[0][1] = -matriz[0][1]
        matriz[1][0] = -matriz[1][0]
        inversa = matriz_x_numero(matriz,1/det_matriz)
    else: 
        for indice,linha in enumerate(matriz): 
            nova_linha = []
            for indiceel,el in enumerate(linha): 
                matriz_aux = []
                for indiceaux, linha_aux in enumerate(matriz): 
                    if indiceaux != indice: 
                        auxl = []
                        for indiceel_aux, elemento in enumerate(linha_aux):
                            if indiceel_aux != indiceel: 
                                auxl.append(elemento)
                        matriz_aux.append(auxl)
                mul *= -1
                det_m = calcula_determinante(matriz_aux)
                try: 
                    el_inversa = det_m[0]*mul/det_matriz
                except Exception as ex: 
                     el_inversa = det_m*mul/det_matriz
                nova_linha.append(el_inversa)
            inversa.append(nova_linha)
    
        inversa = transporta_matriz(inversa)
    return inversa

def inverte_D(matriz): 
    M = vet_para_mat(matriz)
    resultado = []
    for linha in M: 
        auxiliar_linha = []
        for el in linha:
            auxiliar_linha.append(1/el)
        resultado.append(auxiliar_linha)

    resultado = matriz_para_vet(resultado)
    return resultado

def glauss_jacob(matriz, matriz_r, erro,maximo): 
    x_atual = [0,0,0]
    I,S,ID = separa_matriz(matriz)
    SI = soma_matriz(S,I)
    ID = inverte_D(ID)
    J = mul_matriz(matriz_x_numero(ID,-1),SI)
    E = mul_matriz(ID,matriz_r)
    for iteracao in range(0,maximo):
        x_anterior = copy.deepcopy(x_atual) 
        x_atual = soma_matriz(mul_matriz(J,x_anterior),E)
        intervalo_erro = True 
        for indice, i in enumerate(x_atual): 
            difer = m.modulo(i)-m.modulo(x_anterior[indice])
            if m.modulo(difer) > erro:
                 intervalo_erro = False
                 break 
        print(f'{iteracao}-{x_atual}')
        if (intervalo_erro):
            print('achou')
            break
 
def glauss_seidel_mat(matriz,matriz_r,erro,maximo):
    x_atual = []
    for i in matriz: 
        x_atual.append(0)
    I,S,D = separa_matriz(matriz)
    DI = cria_inversa(soma_matriz(I,D))
    G = mul_matriz(matriz_x_numero(DI,-1),S)
    F = mul_matriz(DI,matriz_r)
    for interacao in range(0,maximo): 
        x_anterior =  copy.deepcopy(x_atual) 
        x_atual = soma_matriz(mul_matriz(G,x_anterior),F)
        intervalo_erro = True 
        for indice, i in enumerate(x_atual): 
            difer = m.modulo(i)-m.modulo(x_anterior[indice])
            if m.modulo(difer) > erro:
                 intervalo_erro = False
                 break 
        print(f'{interacao}-{x_atual}')
        if (intervalo_erro):
            print('achou')
            return x_atual
            break

def matriz_x(pontos, grau): 
    Somatorio_grau = []
    for i in range(0,(2*grau+1)):
        if i==0: 
            Somatorio_grau.append(len(pontos))
        else: 
            somatorio = 0 
            for x in pontos: 
                somatorio += x[0]**i
            Somatorio_grau.append(somatorio)

    resultado = []
    for i in range (0,grau+1): 
        linha = []
        for y in range (0,grau+1): 
            linha.append(Somatorio_grau[i+y])
        resultado.append(linha)

    return resultado

def montar_resultado(pontos, grau): 
    resultado = []
    for i in range(0,grau+1): 
        somatorio = 0 
        for x in pontos: 
            somatorio+=(x[0]**i)*x[1]
        resultado.append(somatorio)
    
    return resultado


def ajuste_curva(pontos,grau): 
    matriz = matriz_x(pontos,grau)
    matriz_resultado = montar_resultado(pontos,grau)
    return glauss_seidel_mat(matriz,matriz_resultado, 0.0001, 10000)

def interpolacao(pontos, ponto_descobrir): 
    result  = 0
    for indice, ponto in enumerate(pontos):
        numerador, denominador =  1, 1 
        for indice2, ponto2 in enumerate(pontos): 
            if (indice != indice2): 
                numerador *= (ponto_descobrir - ponto2[0])
                denominador *= (ponto[0]-ponto2[0])
        result += ponto[1]*numerador/denominador
    return result 

def calcula_residuos(pontos,polinomio):
    residuo = 0 
    for ponto in pontos: 
        residuo += abs(ponto[1]-preve_ponto(polinomio,ponto[0]))
    return residuo

def preve_ponto(polinomio, ponto): 
    resultado = 0 
    for i,x in enumerate(polinomio): 
        resultado+=x*(ponto**i)
    return resultado 

def descobre_ponto_ajuste_curva(pontos, grau, ponto_descobrir): 
    polinomio = ajuste_curva(pontos,grau)
    return preve_ponto(polinomio, ponto_descobrir), calcula_residuos(pontos,polinomio)
   

        
