def map_nested(funkcja, lista):
    wynik = []
    for i in lista:
        if isinstance(i, list):
            wynik.append(map_nested(funkcja, i))
        else:
            wynik.append(funkcja(i))
    return wynik

def timesTwo(x):
    return x * 2

lista = [1, [2, 3], [4, [5, 6]]]
razyDwa = map_nested(timesTwo, lista)
print(razyDwa)