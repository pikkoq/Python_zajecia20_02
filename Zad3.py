def recursive_sum(lista):
    total = 0
    for i in lista:
        if isinstance(i,list):
            total += recursive_sum(i)
        else:
            total += i
    return total

liczby = [1, [2,3], [4,[5,6]]]
wynik=recursive_sum(liczby)
print(wynik)