def most_common_element(lst):
    from collections import Counter
    counter = Counter(lst)
    return counter.most_common(1)[0][0]

my_list = [1, 2, 3,3, 2, 4, 2, 5]
common_element = most_common_element(my_list)
print(f"Najczęściej występujący element: {common_element}")
