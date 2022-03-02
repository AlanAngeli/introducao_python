conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
print()

conjunto_intersecao = conjunto.intersection(conjunto2)
print(conjunto_intersecao)
print()

conjunto_diferenca1 = conjunto.difference(conjunto2)
print(conjunto_diferenca1)
print()

conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca2)
print()

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)
print()