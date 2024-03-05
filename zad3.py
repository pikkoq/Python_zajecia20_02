def filter_even_numbers(lista):
    parzyste = [x for x in lista if x % 2 == 0]
    return parzyste
dane = [1,2,3,4,5,6,7,8,9,10]
print(filter_even_numbers(dane))