# List --> Mutable
# Tuple --> Inmutable

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_tuple.append(4) # 'tuple' object has no attribute 'append'

my_tuple.pop(1) # 'tuple' object has no attribute 'pop'

for i in my_tuple:
    print(my_tuple) # 1, 2, 3, 4, 5