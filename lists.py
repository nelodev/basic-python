numbers = [1, 2, 3, 4, 11, 12, 13, 14]
print(numbers)

all_kind_of_stuff = [1, 1.3, "Hi!", True]
print(all_kind_of_stuff)

print(all_kind_of_stuff[2]) # Hi!

print(all_kind_of_stuff[7]) # list index out of range

all_kind_of_stuff.append(False)
print(all_kind_of_stuff) # [1, 1.3, "Hi!", True, False]

all_kind_of_stuff.pop(1)
print(all_kind_of_stuff) # [1, "Hi!", True, False]

for element in all_kind_of_stuff:
    print(element) #1, Hi!, True, False

print(all_kind_of_stuff[::-1]) # [False, True, "Hi!", 1]

print(all_kind_of_stuff[1:2]) # ["Hi!", True]