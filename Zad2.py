def filter_long_words(lista):
    srednia = sum(len(s) for s in lista) / len(lista)
    return [s for s in lista if len(s) > srednia]

stringi = ["jeden", "dwa", "trzy", "cztery"]

przefiltrowane = filter_long_words(stringi)
print(przefiltrowane)