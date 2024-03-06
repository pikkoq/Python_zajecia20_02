def fun(lista):
    lista.sort(key = lambda x : len(x))
    return lista

data = ["Jeden", "Dwa", "Trzy", "Cztery", "Piec", "Szesc","Siedem","Osiem","Dziewiec","Dziesiec"]

sorted = fun(data)
print(sorted)