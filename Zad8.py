def partition_list(lista, funkcja):
    true_part = []
    false_part = []
    for i in lista:
        if funkcja(i):
            true_part.append(i)
        else:
            false_part.append(i)
    return true_part, false_part

def even(x):
    return x % 2 == 0

liczby = [1,2,3,4,5,6]
evenlist, odd = partition_list(liczby,even)
print("Even: ", evenlist)
print("Odd: ", odd)