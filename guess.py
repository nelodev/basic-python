import random

def run():
    random_number = random.randint(1, 100)
    choosen_number = int(input("Choose a number from 1 to 100: "))
    while choosen_number != random_number:
        if choosen_number < random_number:
            print("A bigger number")
        else:
            print("A lower number")
        choosen_number = int(input("Pick another number: "))
    print("You won!")
    

if __name__ == "__main__":
    run()