n1 = int (input('digite o primeiro numero: '))
n2 = int (input('digite o segundo numero: '))
erro = float (input('digite o erro: '))
maximo = int (input('digite o maximo de interações: '))
cont = 0
def f(x): 
    return x*x-9

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
