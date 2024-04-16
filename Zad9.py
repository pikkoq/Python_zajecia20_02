def zip_with_index(input_list):
    return [(item, index) for index, item in enumerate(input_list)]

fruits = ["apple", "banana", "cherry"]
indexed_fruits = zip_with_index(fruits)
print(indexed_fruits) 