def f(x):
  return x-1
  
while (True): 
  n1 = float(input('digite o primeiro numero do intervalo: '))
  n2 = float(input('digite o segundo numero do intervalo: '))
  erro = float(input('digite o numero do erro: '))
  escape = int(input('digite o numero maximo de tentativa: '))
  if (f(n1)*f(n2) < 0): 
    break; 
for i in range (escape):
  media = (n1+n2)/2 
  if (f(media) > -erro and f(media) < erro):
    print(media)
    break;
  if (f(n1)*f(media)<0): 
     n2 = media;  
  else: 
     n1 = media; 
