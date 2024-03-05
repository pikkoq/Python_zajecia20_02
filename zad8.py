import functools

lista = [2,5,7,2,8,11,6]
suma = functools.reduce(lambda x,y : x+y, lista)
print("Suma: ", suma)