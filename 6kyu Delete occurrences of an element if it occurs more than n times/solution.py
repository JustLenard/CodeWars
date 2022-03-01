def delete_nth(order,max_e):
    new_list = order[::-1]

    def remove_from_list(x, new_list, max_e):
        if new_list.count(x) > max_e:
            new_list.remove(x)
            remove_from_list(x, new_list, max_e)
            
    for x in list(dict.fromkeys(new_list)):
        remove_from_list(x, new_list, max_e)
        
    return new_list[::-1]