# counter = 0
# print("2 raised to " + str(counter) + " is equal to: " + str(2**counter))

# counter = 1
# print("2 raised to " + str(counter) + " is equal to: " + str(2**counter))

# counter = 2
# print("2 raised to " + str(counter) + " is equal to: " + str(2**counter))

# counter = 3
# print("2 raised to " + str(counter) + " is equal to: " + str(2**counter))

# counter = 4
# print("2 raised to " + str(counter) + " is equal to: " + str(2**counter))

# counter = 5
# print("2 raised to " + str(counter) + " is equal to: " + str(2**counter))

# WHILE LOOP
def runWhile():
    LIMIT = 1000
    counter = 0
    raised_to_2 = 2**counter
    while raised_to_2 < LIMIT:
        print("2 raised to " + str(counter) + " is equal to: " + str(raised_to_2))
        counter = counter+1
        raised_to_2 = 2**counter

# FOR LOOP
def runFor():
    # for counter in range(2, 10):
    #     print(counter)

    # for i in range(10):
    #     print(11*i)

    # name = input("Write your name: ")
    # for letter in name:
    #     print(letter)

    # phrase = input("Write a phrase: ")
    # for character in phrase:
    #     print(character.upper())

    # for counter in range(1000):
    #     if counter % 2 != 0:
    #         continue
    #     print(counter)
    
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break;

    text = input("Write a phrase: ")
    for letter in text:
        if letter == 'o':
            break
        print(letter)


if __name__ == "__main__":
    # runWhile()
    runFor()
