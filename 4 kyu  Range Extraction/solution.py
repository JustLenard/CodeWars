def solution(args):
    li = []
    my_sol = str(args).replace('[','').replace(']','').replace(' ','')
    for x in args:
        if li == [] or x == li[-1] + 1:
            li.append(x)
        else:
            if len(li) > 2:
                my_sol = my_sol.replace(str(li).replace('[', '').replace(']', '').replace(' ', ''), str(li[0]) + '-' + str(li[-1]))
                li = []
                li.append(x)
            else:
                li = []
                li.append(x)
        if x == args[-1] and len(li) > 2:
            my_sol = my_sol.replace(str(li).replace('[', '').replace(']', '').replace(' ', ''),str(li[0]) + '-' + str(li[-1]))
    return my_sol