# write a function that takes a list of string and returns a new list with each string reversed
# ex: ["abc", "hello"] -> output: ["cba", "olleh"]

def reverse_string(strings):
    reversed_strings = [s[::-1] for s in strings]
    return reversed_strings

str_list_1 = ["Hello", "Python", "Django"]
print(reverse_string(str_list_1))