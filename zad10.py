def generator():
    a=0
    while True:
       yield a
       a += 2

generator_parzystych = generator()
for x in range(100):
    print(next(generator_parzystych))