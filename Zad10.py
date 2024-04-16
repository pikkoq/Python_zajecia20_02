def cumulative_sum(lista):
    wynik = []
    total = 0
    for i in lista:
        total += i
        wynik.append(total)
    return wynik

liczby = [1,2,3,4,5,6]
suma = cumulative_sum(liczby)
print(suma)