def split_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunked_numbers = split_list(numbers, 3)
print(chunked_numbers) 