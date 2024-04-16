def flatten_list(lista):
    plaska = []
    for i in lista:
        if isinstance(i, list):
            plaska.extend(flatten_list(i))
        else:
            plaska.append(i)
    return plaska

liczby = [1, [2, 3], [4, [5, 6]]]
wynik = flatten_list(liczby)
print(wynik)