import math

def function(n):
    elemento_cabecilla = 1
    for i in range (1, n):
        print(n)
        razon  = 2 ** i
        cardinalidad = math.ceil(n/razon)
        if cardinalidad == 1:
            break
        if i % 2 == 0:
            elemento_cabecilla -= ((cardinalidad-1)*razon)
        else:
            elemento_cabecilla += ((cardinalidad-1)*razon)
        
    return elemento_cabecilla

def func2(n):
    z=[]
    for a in range (1, n+1):
        z.append(a)
    a=z
    i=1
    while len(a)>1:
        if i%2==0:
            a=a[::-2]
            a.reverse()
        else:
            a=a[::2]
        print(a)
        i+=1
while(1):
    n = int(input())
    print(function(n))
    #func2(n)