import random
import time
list = [random.randint(1,1000) for x in range(1000)]

def sort_insert(list):
    for j in range(len(list)):
        key = list[j]
        i = j-1
        while list[i] > key and i >=0:
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key
    return list



start = time.time()
print(sort_insert(list))
end = time.time()
print(end-start)