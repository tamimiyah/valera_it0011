# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-24

import os

#Opens the "students.txt" file in read mode.
file_path = os.path.join(os.path.dirname(__file__), "students.txt")
with open(file_path, "r") as file:
    print("\nREADING STUDENT INFORMATION")
    for line in file:
        # Reads the contents of the file.
        parts = line.strip().split("  ")
        lname = parts[0].split(": ")[1].split(", ")[0]
        fname = parts[0].split(": ")[1].split(", ")[1]
        age = parts[1].split(": ")[1]
        contactNum = parts[2].split(": ")[1]
        course = parts[3].split(": ")[1]
        
        #Displays the student information to the user
        print(f"\nFULL NAME: {lname.upper()}, {fname.upper()}")
        print(f"AGE: {age}")
        print(f"CONTACT #: {contactNum}")
        print(f"COURSE: {course.upper()}")