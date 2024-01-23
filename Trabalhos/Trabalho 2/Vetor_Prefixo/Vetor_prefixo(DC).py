import time


inicio = time.time()


def max_prefixo_DC(vet, esq, dir):
    if esq == dir:
        return vet[esq]
    mid = (esq + dir) // 2
    return max_prefixo_DC(vet, esq, mid) + max_prefixo_DC(vet, mid + 1, dir)

def max_prefixo_DC(vet, n):
    if n == 0:
        return ""
    prefixo = [0] * (n + 1)
    len1 = len(vet[0])
    prefixo[1] = len1
    x = prefixo[1]
    for i in range(2, n + 1):
        len1 = len(vet[i - 1])
        len2 = len(vet[i - 2])
        count = 0
        while (count < len1 and count < len2):
            if (vet[i - 1][count] != vet[i - 2][count]):
                break
            count += 1
        prefixo[i] = count
        x = min(x, prefixo[i])
    return vet[0][:x]


vet = ["flagra", "flacido", "flanela", "flagelo", "flatulência", "flamingo", "flanco", "flauta", "flamenguista"]
n = len(vet)
print("Prefixo: ", max_prefixo_DC(vet, n))

fim = time.time()
print("Tempo de execução = ",fim-inicio)

