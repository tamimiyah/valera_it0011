# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-24

import os

# Accepts input for the last name, first name, age, contact number, and course from the user.

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
        print("Invalid input. Please enter a valid last name (letters and spaces only).")       
       
age = int(input("Enter Age: "))

while True:
    contactNum = input("Enter Contact Number: ")
    if contactNum.isdigit() and len(contactNum) == 11:
        break
    else:
        print("Invalid input. Please enter an 11-digit number.")
        
while True:
    course = input("Enter Course: ")
    if all(part.isalpha() for part in course.split()):
        break
    else:
        print("Invalid input. Please enter a valid course name (letters and spaces only).")

# Creates a string containing the collected information in a formatted way.
student = f"Full Name: {lName.capitalize()}, {fName.capitalize()}  Age: {age}  Contact #: {contactNum}  Course: {course.capitalize()}"

# Opens a file named "students.txt" in append mode and writes the formatted information to the file.
file_path = os.path.join(os.path.dirname(__file__), "students.txt")
with open(file_path, "a+") as file:
    file.write(student + "\n")
    # Displays a confirmation message indicating that the information has been saved.
    print(f"Student Information has been saved successfully to '{file_path}'!")