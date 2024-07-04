# Write a function that takes only a list of intergers and return a new list that contains only even number of the original list

def get_even_number(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(get_even_number(list_1))