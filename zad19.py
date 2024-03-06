def add(tup, x):
    temp = tup + (x,)
    return temp

tuple = (1, 2, 3)
new_tuple = add(tuple, 11)
print(f"Stara: {tuple}")
print(f"Nowa: {new_tuple}")