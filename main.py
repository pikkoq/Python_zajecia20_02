from zadanie2 import *
#zadanie 2
print("Zadanie2")
splitwords("siemanko witam w mojej kuchni")

checkif(5, 4)

#zadanie 3
print("Zadanie3")
x = 55

def infunction():
    x = 11
    print("Wartość x w funkcji: ", x)
infunction()
print("Wartość x poza funkcją: ", x)

#zadanie 4
print("Zadanie4")
def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def run(fn,a,b):
    return fn(a,b)

r1 = run(add,5,5)
r2 = run(subtraction,5,5)
print(r1, r2)

#zadanie 5
print("Zadanie 5")

lista = [1,2,3,4,5,6,7,8,9,10]
def even(list):
    for num in list:
        if num % 2 == 0:
            print(num)
even(lista)

x = lambda a,b: a*b
print("Pole prostokąta równe", x(5, 5))

#zadanie 6
print("Zadanie 6")

listaSlow = ["Dzien", "Dobry", "Awokado", "Ananas", "Banan"]

def zaczyna(word):
    if word[0] == "A":
        return True
    else:
        return False
slowaA = filter(zaczyna,listaSlow)
for x in slowaA:
    print(x)


def kwadratliczb(n):
    return n * n

numbers = (1, 2, 3, 4)
listakwadratow = map(kwadratliczb, numbers)
print(list(listakwadratow))

#zadanie 7
print("Zadanie 7")

data = [1,2,3,4,5,6]
def kwadrat(x):
    return x * x
def dodaj(x):
    return x + 5

def add(x,y):
    return x+y

def apply(data):
    data = map(kwadrat, data)
    data = map(dodaj, data)
    return list(data)

def doFunction(fun ,arg):
    for f, v in zip(fun, arg):
        print(f(*v) if isinstance(v, tuple) else f(v))