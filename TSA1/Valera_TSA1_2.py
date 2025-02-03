#AUTHOR: VALERA, TAMIYAH GALE C.
#DATE: 2025-02-03

#Problem 2: A program that will count the sum of the digits from a given input string digits. (use for loop and some operators under module 1 and 2)

print("\n************************************************************")
userInput = input("Enter a string of digits: ")
print("************************************************************")

sum = 0

for i in userInput:
    if i.isdigit():
        sum += int(i)

print("\nThe sum of the digits is: ", sum)

