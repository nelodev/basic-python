def isPrime(newNumber):
    counter = 0
    for i in range(1, newNumber+1):
        if i == 1 or i == newNumber:
            continue
        if newNumber % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

def run():
    newNumber = int(input("Write a number: "))
    if isPrime(newNumber):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    run()