# write a function that takes two dictionaries and merge them into one. If a key exists in both dictionaries, the value from the second dictionary should be used

def merge_dicts(dict1,dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


dict1 = {"a": 1 , "b" : 2}
dict2 = {"b": 3 , "d" : 4}
print(merge_dicts(dict1,dict2))
