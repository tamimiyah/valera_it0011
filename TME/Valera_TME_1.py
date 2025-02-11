#AUTHOR: VALERA, TAMIYAH GALE C.
#DATE: 2025-02-11

#Create a program that will open the file numbers.txt.
#Check each line if the sum of the given string digit numbers is palindrome.

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def sum_of_digits(line):
    numbers = line.split(',')
    total = sum(int(number) for number in numbers)
    return total   

#Open the file numbers.txt
with open("c:/Users/Tamiyah Valera/OneDrive/Documents/GitHub/valera_it0011/TME/numbers.txt", "r") as file:
    #Read the file
    lines = file.readlines()

    #Check each line
    for line in lines:
        total = sum_of_digits(line)
        if is_palindrome(total):
            print(f"\nLINE {lines.index(line)+1}:\n {line.strip()}' is (sum {total}) - Palindrome.")
        else:
            print(f"\nLINE {lines.index(line)+1}:\n {line.strip()}' is (sum {total}) - Not Palindrome.")

