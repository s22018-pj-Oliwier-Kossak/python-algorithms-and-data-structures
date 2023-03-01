from functools import reduce

numbers = [1,45,672,7265,16]
sorted_numbers = sorted(numbers, key = lambda x: x%10)
print(sorted_numbers)

codes = ['JPID', 'JJJPPP', 'XXX', 'JDU']

reduceCodes = reduce(lambda x,y: x if len(x) >len(y) else y,codes)
print(reduceCodes)

capitals =['Rome', 'Paris', 'Madrid']
cities = ['Rome', 'Napoli', 'Rimini', 'Paris', 'Barcelona', 'Madrid', 'Marceille']

sameCities = list(filter(lambda x: x not in capitals,cities))
print(sameCities)