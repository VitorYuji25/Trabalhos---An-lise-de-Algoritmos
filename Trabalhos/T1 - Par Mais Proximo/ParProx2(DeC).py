import math
import copy
from random import randint
import time
#Divisão e conquista com a ordenação "simples" em cada chamada (informalmente vimos que esta solução tem complexidade O(n(lg n)^2) 
# O algoritmo divide todos os pontos em dois conjuntos e chama recursivamente. Depois de dividir, ele encontra tempo O (nLogn) e finalmente encontra os pontos mais próximos na faixa no tempo O (n). 
# Portanto, T (n) pode ser expresso da seguinte forma: 
#T (n) = 2T (n / 2) + O (n) + O (nLogn) + O (n) 
#T (n) = 2T (n / 2) + O (nLogn ) 
#T (n) = T (nx Logn x Logn) = O(n(lg n)^2)

#Start do cronometro
start_time = time.perf_counter()

class Point():
    def __init__(point, x, y):
        point.x = x
        point.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))
 

def FB(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
 
    return min_val
 
def smaisProx(s, tam, d):
    min_val = d
    for i in range(tam):
        j = i+1
        while j < tam and ((s[j].y) - (s[i].y)) < min_val:
            min_val = dist(s[i], s[j])
            j += 1
 
    return min_val
 
def maisProxEntre(P, Q, n):
    if n <= 3:
        return FB(P, n)
    mid = n // 2
    midPoint = P[mid]
    pl = P[:mid]
    pr = P[mid:]
    dl = maisProxEntre(pl, Q, mid)
    dr = maisProxEntre(pr, Q, n - mid)
    d = min(dl, dr)
    sP = []
    sQ = []
    r = pl + pr
    
    for i in range(n):
        if abs((r[i].x) - (midPoint.x)) < d:
            sP.append(r[i])
        if abs((Q[i].x) - (midPoint.x)) < d:
            sQ.append(Q[i])
 
    sP.sort(key = lambda point: point.y) #ordenado por y
    min_a = min(d, smaisProx(sP, len(sP), d))
    min_b = min(d, smaisProx(sQ, len(sQ), d))
     
    return min(min_a,min_b)
 

def maisProx(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)   

    return maisProxEntre(P, Q, n)
P = []
tam = int(input("Digite a quantidade de ponto no plano: "))
for k in range (tam):
    P.append(Point(randint(1,1000000),randint(1,1000000)))
n = len(P)
print("Menor distancia eh:",maisProx(P, n))
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Programa executado em: {execution_time: .5f} segundos")