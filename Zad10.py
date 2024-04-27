import itertools

def all_permutations(lst):
    return list(itertools.permutations(lst))

my_list = [1, 2, 3]
permutations_list = all_permutations(my_list)
print(f"Wszystkie permutacje listy: {permutations_list}")
