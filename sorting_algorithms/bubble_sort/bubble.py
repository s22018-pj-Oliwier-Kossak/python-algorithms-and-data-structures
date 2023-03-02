import  random
import time
list = [random.randint(1,100) for x  in range(2000)]
list2 = list.copy()
print(list)
def buble(list):
    change =True
    while change:
        change = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                change = True

def buble2(list):
    change = True
    max_index = len(list)-1
    for i in range(max_index,0,-1):
        for i in range (max_index):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                change = True
        if not change:
            break




start = time.time()
buble(list)
print(list)
stop = time.time()
print(f'sort time {stop - start  }')

start = time.time()
buble2(list2)
print(list2)
stop = time.time()
print(f'sort time {stop - start  }')

