list =[4,1,31,2]




def linear_search(list,value):
    found = False
    i = 0
    while not found and i < len(list):
        if list[i] == value:
            found = True
        else:
            i += 1
    return f'index: {i} ,value: {value}' if i < len(list) else None
print(linear_search(list,2))


