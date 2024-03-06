from functools import partial


def dodawanie(x,y):
    return x+y
wynik = partial(dodawanie,5)
print(wynik(10))