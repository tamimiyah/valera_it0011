# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-24

#Input the user's first name and last name.

while True:
    fName = input("Enter First Name: ")
    if all(part.isalpha() for part in fName.split()):
        break
    else:
        print("Invalid input. Please enter a valid first name (letters and spaces only).")

while True:
    lName = input("Enter Last Name: ")
    if all(part.isalpha() for part in lName.split()):
        break
    else:
        print("Invalid input. Please enter a valid first name (letters and spaces only).")  
        
#Concatenate the input names into a full name.
fullName = fName + " "+ lName
print(f"\nFull Name: {fullName}")

#Display the full name in both upper and lower case.
print(f"\nFull Name(Upper Case): {fullName.upper()}")
print(f"\nFull Name(Lower Case): {fullName.lower()}")

#Count and display the length of the full name
print(f"\nFull Name Length: {len(fullName)}") #Spaces are included in the length

