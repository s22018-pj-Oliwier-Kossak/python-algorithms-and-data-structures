
list = [1,2,3,4,6,7,10]

def interpolation_search(list,value):
    start = 0
    end = len(list)-1
    found = False


    while not found and start <=end and value >= list[start] and value <= list[end]:

        if list[start] != list[end]:
            mid = start + int((float(end - start) / (list[end] - list[start])) * (value - list[start]))
        else:
            mid = start

        if list[mid] == value:
            found = True
        else:
            if value > list[mid]:
                start = mid + 1
            else:
                end = mid - 1

    if  found:
        return True
    else:
        return False

print(interpolation_search(list,10))



