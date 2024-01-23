from random import randint
import time


inicio = time.time()

def target_sum(V, k):
    count = 0
    subset = []

    def subvet(i, k1):
        nonlocal count
        if k1 == k:
            count += 1
            subset.append(list(numbers))
        if k1 < k and i < len(V):
            numbers.append(V[i])
            subvet(i + 1, k1 + V[i])
            numbers.pop()
            subvet(i + 1, k1 - V[i])

    numbers = []
    subvet(0, 0)

    return count


# Example usage:
v=[]
for i in range(25):
        random_number = randint(0, 10)
        v.append(random_number)
print(v)
print("Digite o valor de k: ")
k = int(input())
print(target_sum(v, k))

fim = time.time()
print("Tempo de execução = ",fim-inicio)