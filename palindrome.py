def checkPalindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False

def run():
    word = input('Write a word to check if is palindrome: ')
    isPalindrome = checkPalindrome(word)
    if isPalindrome:
        print("Is palindrome")
    else:
        print("Is not palindrome")

if __name__ == "__main__":
    run()