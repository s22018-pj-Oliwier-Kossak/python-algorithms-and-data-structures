import time
max_limit = 50000
my_list = list(range(max_limit))
my_set = set(range(max_limit))
number = 500


start = time.time()
for number in range(len(my_list)):
    is_number = number in my_list
stop = time.time()
print(f'Operation duration was {stop - start}')

start = time.time()
for number in range(len(my_set)):
    is_number = number in my_set
stop = time.time()
print(f'Operation duration was {stop - start}')