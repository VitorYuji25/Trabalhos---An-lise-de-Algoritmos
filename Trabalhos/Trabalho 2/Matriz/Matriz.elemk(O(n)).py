import random

import time


inicio = time.time()

def check_matriz(matriz, k):
    n = len(matriz)
    m = len(matriz[0])

    linha = 0
    coluna = m - 1

    while linha < n and coluna >= 0:
        if matriz[linha][coluna] == k:
            return True
        elif matriz[linha][coluna] > k:
            coluna -= 1
        else:
            linha += 1

    return False


linhas = 200
# Cria a matriz e preenche 
matriz = []
for i in range(200):
    matriz.append(sorted(random.sample(range(0, 10000), 200)))

# Imprime a matriz
for linha in matriz:
    print(linha)

print("Digite o valor a ser encontrado: ")
k = int(input())


print(check_matriz(matriz,k))

fim = time.time()
print("Tempo de execução = ",fim-inicio)