def guess_gifts(w, p): 
    may_get = []
    for x in p:
        for i in w:
            if (x['size'] == i['size'] and 
                x['clatters'] == i['clatters'] and 
                x['weight'] == i['weight'] and 
                i['name'] not in may_get):
                    may_get.append(i['name'])
    return may_get