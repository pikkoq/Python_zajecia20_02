def add(x):
    def a(y):
        print(x, y)
    return a

add(5)(10)