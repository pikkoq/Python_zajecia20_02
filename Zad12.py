def rotate_list(lista, krok):
    n = len(lista)
    krok %= n
    return lista[-krok:] + lista[:-krok]

liczby =[1,2,3,4,5]
zamien = rotate_list(liczby,2)
print(zamien)