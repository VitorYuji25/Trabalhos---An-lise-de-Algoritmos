from random import randint
import time


inicio = time.time()
def target_sum(V, K):
    # Criar tabela para armazenar sub-soluções
    R = [[0 for _ in range(K+1)] for _ in range(len(V)+1)]
   
    # Ao inicializar a tabela, todos os subconjuntos vazios tem a soma 0
    for i in range(len(V)+1):
        R[i][0] = 1
   
    # Iterar por cada elemento do vetor e calcular sub-soluções
    for i in range(1, len(V)+1):
        for j in range(1, K+1):
            if V[i-1] <= j:
                # Se o elemento atual for menor ou igual ao valor j, então escolher incluí-lo
                R[i][j] = R[i-1][j-V[i-1]] + R[i-1][j]
            else:
                R[i][j] = R[i-1][j]
   
    # Retornar o número de combinações possíveis
    return R[-1][-1]




v=[]
for i in range(1000):
        random_number = randint(0, 10)
        v.append(random_number)
print(v)
print("Digite o valor de k: ")
k = int(input())
print(target_sum(v, k))


fim = time.time()
print("Tempo de execução = ",fim-inicio)