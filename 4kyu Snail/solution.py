def snail(snail_map):
    sol = []
    while snail_map != []:
        for ar in snail_map:
            if ar == snail_map[0] :
                sol.extend([x for x in ar])
                ar.clear()
            elif ar != snail_map[0] and ar != snail_map[-1] :
                sol.append(ar[-1])
                ar.pop(-1)
            elif ar == snail_map[-1] :
                sol.extend([x for x in reversed(ar)])
                ar.clear()
        for ar in snail_map:
            if ar == []:
                snail_map.remove([])
        for ar in reversed(snail_map):
            try:
                sol.append(ar[0])
                ar.pop(0)
            except:
                pass
        for ar in snail_map:
            if ar == []:
                snail_map.remove([])
    return sol