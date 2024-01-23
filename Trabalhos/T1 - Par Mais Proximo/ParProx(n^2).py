#Instruções
#Implementar a resolução para o Problema do Par Mais Proximo  usando  as seguintes abordagens:

#Busca exaustiva com todos os pares, com complexidade O(n^2);

import math
from random import randint
import time

#Start do cronometro
start_time = time.perf_counter()
tam = int(input("Digite a quantidade de ponto no plano: "))
X = []
Y = []
k = int
par = [1]
for k in range (tam):
        X.append(randint(1,10000000))
        Y.append(randint(1,10000000))
#print(X,Y)

def Dist(elemX1,elemY1,elemX2,elemY2):
        return abs(math.sqrt((elemX1 - elemX2) * (elemX1 - elemX2) + (elemY1 - elemY2) * (elemY1 - elemY2)))
         
    

def ParProx(X,Y): 
    d = 10000
    for i in range (2 , tam):
        for j in range (1 , i-1):
            if (Dist(X[i],Y[i],X[j],Y[j]))<d:
                d = Dist(X[i],Y[i],X[j],Y[j])
                par[0] = (X[i],Y[i]),(X[j],Y[j])
    return d
    
print("Menor distancia:", ParProx(X,Y))
print("O par mais proximo eh: ", par)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Programa executado em: {execution_time: .5f} segundos")