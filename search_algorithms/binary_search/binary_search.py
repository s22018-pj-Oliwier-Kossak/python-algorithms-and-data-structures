list = [x for x in range(1,10)]
print(len(list))
def binary_search(list,value):
    start = 0
    end = len(list)-1
    found = False

    while not found and start <= end:
        mid = (end + start) // 2
        if list[mid] == value:
            found = True
        else:
            if value > list[mid]:
                start = mid+1
            else:
                end = mid-1

    if found:
        return True
    else:
        return False

print(binary_search(list,100))


