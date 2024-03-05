def apply_twice(funkcja, wartosc):
    return funkcja(funkcja(wartosc))
wynik = apply_twice(lambda x : x+5, 5)
print(wynik)