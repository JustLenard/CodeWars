def valid_solution(b):
#   Checking the Rows
    for x in b:
        if len(set(x)) != 9: return False 
#   Checking the Colums
    for x in range(9):
        if len(set([i[x] for i in b])) != 9: return False
#    Checking the 3x3 'squares'
    magik = [0, 3, 6]
    for x in magik:
        li = []
        for i in b[x:x+3]:
            for z in i[x:x+3]:
                li.append(z)
        if len(set(li)) != 9: return False
    return True