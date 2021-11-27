# test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
# test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
# test.assert_equals(sort_array([]),[])

def sort_array(source_array):
    odd = [x for x in source_array if x % 2 == 1]
    odd.sort()
    count = 0
    new = []
    for x in range(len(source_array)): 
        if source_array[x] % 2 == 1:
            new.append(odd[count])
            count += 1
        else:
            new.append(source_array[x])
    return new