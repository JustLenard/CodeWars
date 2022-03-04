def comp(array1, array2):
    if array1 == array2 == []: return True
    return False if array1 == None or array1 == [] else sorted([x**2 for x in array1]) == sorted(array2)