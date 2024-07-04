# Write a function that takes two sets and returns their common value
def set_common(set1, set2):
    return set1.intersection(set2)


set1 = {1,2,3}
set2 = {6,4,5}
print(set_common(set1, set2))