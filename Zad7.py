from itertools import groupby

liczby = [1, 2, 3, 4, 5, 6, 7, 8,9]

liczby_posortowane = sorted(liczby, key=lambda x: x % 2)

zgrupowane_liczby = {k: list(v) for k, v in groupby(liczby_posortowane, key=lambda x: x % 2)}

print(zgrupowane_liczby)