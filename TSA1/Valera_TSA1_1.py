#AUTHOR: VALERA, TAMIYAH GALE C.
#DATE: 2025-02-03

#Problem 1: A program that will display the number of vowels, consonants, spaces, and other characters given an input string. (use for loop and some operators under module 1 and 2)

print("\n************************************************************")
userInput = input("Enter a string: ")
print("************************************************************")
vowels = 0
consonants = 0
spaces = 0
others = 0

for i in userInput:
    if i in "aeiouAEIOU":
        vowels += 1
    elif i == " ":
        spaces += 1
    elif i.isalpha():
        consonants += 1
    else:
        others += 1
        
print("\nVowels: ", vowels)

print("Consonants: ", consonants)

print("Spaces: ", spaces)

print("Other Characters: ", others)

