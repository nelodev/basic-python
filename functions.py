# def print_message():
#     print("Special message: ")
#     print("I'm learning how to use functions!")

# print_message()
# print_message()
# print_message()

# def conversation(option):
#     print("Hi! 😊")
#     print("How are you?")
#     print("You've chosen option " + str(option))
#     print("Bye!")

# option = int(input('Choose an option (1, 2, 3): '))
# conversation(option)

def suma(a, b):
    print('Two numbers are added, ' + str(a) + " and " + str(b))
    result = a+b
    return result

totalSum = suma(1,4)
print("Result: " + str(totalSum))
