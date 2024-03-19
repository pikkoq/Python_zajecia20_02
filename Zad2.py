from itertools import combinations

def combination(lista):
    return list(combinations(lista,2))

tab = ["A", "B", "C", "D", "E"]
print(combination(tab))