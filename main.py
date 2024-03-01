import functools

import lorem_text.lorem

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

data = [1,2,3,4,5,6]
doFunction([kwadrat, dodaj, add], [5,10, (10, 15)])

#zadanie 8
print("Zadanie 8")

liczbyKwadratowe = [x*x for x in range(1, 11)]
print(liczbyKwadratowe)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
length = [len(slowo) for slowo in fruits]
print(length)

#zadanie 9
print("Zadanie 9")

def dziewiate():
    lista = [2,5,7,2,8,11,6]
    print("Najwieksza liczba: ", functools.reduce(lambda a,b: a if a > b else b, lista))
    srednia = functools.reduce(lambda x,y : x+y, lista) / len(lista)
    print("Srednia: ", srednia)
dziewiate()

#zadanie 10
print("Zadanie 10")

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator_fib = fib()
for x in range(1000):
    print(next(generator_fib))

def write(filename):
    with open(filename, "w") as file:
        for x in range(1000):
            file.write(lorem_text.lorem.paragraph() + '\n\n')
#write("lorem.txt")

def read(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
for line in read("lorem.txt"):
    print(line)