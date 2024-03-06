from functools import partial


def mnozenie(x,y):
    return x*y

dzialanie = partial(mnozenie, 3)
print(dzialanie(9))