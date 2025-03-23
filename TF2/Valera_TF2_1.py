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
        
age = int(input("Enter Age: "))

        
#Concatenate the input names into a full name.
print(f"\nFull Name: {fName.capitalize()} {lName.capitalize()}")


#Slice the full name to extract the first three characters of the first name.
slicedName = fName[:3]
print("Sliced Name: " + slicedName.capitalize())

#Use string formatting to create a greeting message that includes the sliced first name

print(f"\nGreeting Message: Hello {slicedName}, Welcome! You are {age} years old.")