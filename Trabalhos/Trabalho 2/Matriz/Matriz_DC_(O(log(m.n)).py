import random

def busca_binaria(vet, esq, dir, k):
    if dir >= esq:
        mid = (dir + esq) // 2
        if vet[mid] == k:
            return True
        elif vet[mid] > k:
            return busca_binaria(vet, esq, mid - 1, k)
        else:
            return busca_binaria(vet, mid + 1, dir, k)
    else:
        return False

def search(mat, n, m, k):
    esq = 0
    dir = n * m - 1
    while esq <= dir:
        mid = (dir + esq) // 2
        if mat[mid // m][mid % m] <= k:
            esq = mid + 1
        else:
            dir = mid - 1

    i = 0
    j = 0
    while i < n and j < m:
        if mat[i][j] <= k:
            j += 1
        else:
            i += 1

    if i < n:
        if busca_binaria(mat[i], 0, m - 1, k):
            return True

    if j < m:
        if busca_binaria(mat[i - 1], 0, m - 1, k):
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


print(search(matriz,linhas,colunas,k))