
import random


def check_in_matriz(matriz, k):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == k:
                return True
    return False


# Define o tamanho da matriz
linhas = 100
colunas = 100

# Cria a matriz e preenche 
matriz = []
for i in range(200):
    matriz.append(sorted(random.sample(range(0, 10000), 200)))

# Imprime a matriz
for linha in matriz:
    print(linha)

print("Digite o valor a ser encontrado: ")
k = int(input())


print(check_in_matriz(matriz,k))