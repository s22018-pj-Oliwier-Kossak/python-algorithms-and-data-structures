names = ['John Johnson', 'Alicja Policja', 'Wladimir Wladymirowicz']

x = names[0].split(' ')
print(x)
def get_sub_name(name,part):
    first_name = name.split(' ')
    return first_name[part]


print(get_sub_name(names[0],1))

listLastName = [get_sub_name(x,1) for x in names]
listFirstName = [get_sub_name(x,0) for x in names]
print(listFirstName)
print(listLastName)

listLastNameLambda = [(lambda name:name.split(' ')[1])(x) for x in names]
listFirstNameLambda = [(lambda name:name.split(' ')[0])(x) for x in names]
print(listLastNameLambda)
print(listFirstNameLambda)

listLastNameGenerator = [name.split(' ')[0] for name in names]
listFirstNameGenerator = [name.split(' ')[1] for name in names]
print(listLastNameGenerator)
print(listFirstNameGenerator)