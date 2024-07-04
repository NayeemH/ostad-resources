# Write a function that takes a list of tuples, each touple contains two integers, and returns a list of tuples with element swapped
# ex: list_of_tuple = [(1,2), (3,4)] -> [(2,1), (4,3)]

def swap_tuples(tuples):
    swapped = [(b,a) for a,b in tuples]
    return swapped

tuples = [(1,2), (3,4), (5,6)]
print(swap_tuples(tuples))