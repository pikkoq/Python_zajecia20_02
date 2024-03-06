def compose(fun1, fun2):
    return lambda x : fun1(fun2(x))

def fun1(x):
    return x+2
def fun2(x):
    return x*5

wynik = compose(fun1,fun2)
print(wynik(5))