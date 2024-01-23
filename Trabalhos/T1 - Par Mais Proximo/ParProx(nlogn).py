# Divisao e Conquista usando a tecnica "pig back": 
# "aproveitar" as recursões e trocar a ordenação - 
# que gasta O(n lgn) por chamada - , por um merge menos complexo, 
# resultando em um algoritmo final O(n lg n) 

import copy
import math
from random import randint
import time
    
    

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].x < righthalf[j].x and lefthalf[i].y < righthalf[j].y:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist


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
    mergeSort(P)
    Q = copy.deepcopy(P)

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