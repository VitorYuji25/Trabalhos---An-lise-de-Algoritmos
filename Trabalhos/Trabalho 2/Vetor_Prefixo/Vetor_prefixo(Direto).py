import time


inicio = time.time()

def max_prefixo(vetor):
    prefixo = vetor[0]
    for string in vetor[1:]:
        while string[:len(prefixo)] != prefixo and prefixo:
            prefixo = prefixo[:len(prefixo)-1]
        if not prefixo:
            break
    return prefixo


vetor = ["abacateiro"
,"abacateiroso"
,"abacateirosofia"
,"abacateirosofialidade"
,"abacateirosofialidadedos"
,"abacateirosofialidadedosolhos"
,"abacateirosofialidadedosolhosverdes"
,"abacateirosofialidadedosolhosverdesde"
,"abacateirosofialidadedosolhosverdesdeum"
,"abacateirosofialidadedosolhosverdesdeumgato"]

print("O maior prefixo comum é ", max_prefixo(vetor))

fim = time.time()
print("Tempo de execução = ",fim-inicio)