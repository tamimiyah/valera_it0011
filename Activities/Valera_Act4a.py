# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-23

import os

# Global variables for student records
studentRecords = []

# Global variable to store the current file name
currentFile = ""


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def calcGrade(studentClassStanding, studentExamScore):
    return (0.6 * studentClassStanding) + (0.4 * studentExamScore)

def continuePrompt(promptInsert):
    while True:
        choice = input("\nDo you want to " + promptInsert + "? (y/n): ").strip().lower()
        if choice == 'y':
            if promptInsert.strip().lower() == "open another file":
                openFile()
            elif promptInsert.strip().lower() == "save new file":
                saveFile()
            elif promptInsert.strip().lower() == "save in another file":
                saveAsFile()
            elif promptInsert.strip().lower() == "show and sort again":
                showAllRecords()
            elif promptInsert.strip().lower() == "show another record":
                showRecord()
            elif promptInsert.strip().lower() == "add another record":
                addRecord()
            elif promptInsert.strip().lower() == "edit another record":
                editRecord()
            elif promptInsert.strip().lower() == "delete another record":
                deleteRecord()
        elif choice == 'n':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    clearScreen()

def main_menu():
    clearScreen()
    while True:
        print("\n************************************************************")
        print("\t\tSTUDENT MANAGEMENT SYSTEM")
        print("************************************************************")
        print("\n1. Open File")
        print("2. Save File (New File)")
        print("3. Save as File (Existing File)")
        print("4. Show All Students Record")
        print("5. Show a Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == "1":
            openFile()
        elif choice == "2":
            saveFile()
        elif choice == "3":
            saveAsFile()
        elif choice == "4":
            showAllRecords()
        elif choice == "5":
            showRecord()
        elif choice == "6":
            addRecord()
        elif choice == "7":
            editRecord()
        elif choice == "8":
            deleteRecord()
        elif choice == "9":
            print("Exiting Program....")
            break
        else:
            print("Invalid Choice. Please Try Again!!!")
               
def openFile():
    global currentFile
    clearScreen()
    print("Existing files in the directory:")
    fileNameSSS = [file for file in os.listdir() if os.path.isfile(file)]
    for file in fileNameSSS:
        print(file)
        
    fileName = input("Enter the file name to open: ")
    if os.path.exists(fileName):
        with open(fileName, "r+") as file:
            global student_records
            student_records = []
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    studentId, studentLastName, studentFirstName, studentClassStanding, studentExamScore = data
                    student_records.append((studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore))
        currentFile = fileName
        print(f"File '{fileName}' loaded successfully!")
    else:
        print(f"File '{fileName}' does not exist.")

    continuePrompt("Open Another File")
            
def saveFile():
    clearScreen()
    while True:
        fileName = input("Enter the Filename to save: ")
        if not os.path.exists(fileName):
            with open(fileName, "w+") as file:
                for record in studentRecords:
                    studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
                    file.write(f"{studentId},{studentLastName},{studentFirstName},{studentClassStanding},{studentExamScore}\n")
            print(f"Records saved successfully to '{fileName}'!")
            break
        else:
            print(f"File '{fileName}' already exists. Please enter a different file name.")
    continuePrompt("Save New File")    

def saveAsFile():
    clearScreen()
    while True:
        print("Existing files in the directory:")
        fileNameSSS = [file for file in os.listdir() if os.path.isfile(file)]
        for file in fileNameSSS:
            print(file)
        
        fileName = input("Enter the Filename Where You Want it to Save (must be an existing file): ")
        if fileName in fileNameSSS:
            with open(fileName, "a+") as file:
                for record in studentRecords:
                    studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
                    file.write(f"{studentId},{studentLastName},{studentFirstName},{studentClassStanding},{studentExamScore}\n")
            print(f"Records saved successfully to '{fileName}'!")
            break
        else:
            print(f"File '{fileName}' does not exist. Please enter a valid filename from the list.")
    continuePrompt("save in another file")

####NOTES: Before opening showAllRecords function and choosing 4 in Main Menu, Make Sure that you have opened a file first.       
def showAllRecords():
    clearScreen()
    print(f"Showing records from file: {currentFile}")
    print("Sort the Records by:")
    print("1. Last Name (Ascending)")
    print("2. Last Name (Descending)")
    print("3. Grades (Ascending)")
    print("4. Grades (Descending)")
    
    while True:
        choice = input("Enter Choice: ")
        
        if choice == "1":
            sorted_records = sorted(student_records, key=lambda x: x[1][0].lower()) # Sort from A to Z
            break
        elif choice == "2":
            sorted_records = sorted(student_records, key=lambda x: x[1][0].lower(), reverse=True) # Sort from Z to A
            break
        elif choice == "3":
            sorted_records = sorted(student_records, key=lambda x: calcGrade(float(x[2]), float(x[3]))) # Sort from 0 to 100
            break
        elif choice == "4":
            sorted_records = sorted(student_records, key=lambda x: calcGrade(float(x[2]), float(x[3])), reverse=True) # Sort from 100 to 0
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    for record in sorted_records:
        studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
        studentGrade = calcGrade(float(studentClassStanding), float(studentExamScore))
        print(f"ID: {studentId}, Name: {studentLastName.capitalize()}, {studentFirstName.capitalize()}, "
              f"Class Standing: {studentClassStanding}, Exam Score: {studentExamScore}, Grade: {studentGrade}")
    
    continuePrompt("Show and Sort Again")

####NOTES: Before opening showRecord function and choosing 5 in Main Menu, Make Sure that you have opened a file first. 
def showRecord():
    clearScreen()
    print(f"Showing records from file: {currentFile}")
    
    # Find a specific student based on their student ID
    studentID = input("Input Student ID to show record: ")
    
    # Search for the student record
    found = False
    for record in student_records:
        if record[0] == studentID:
            studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
            studentGrade = calcGrade(float(studentClassStanding), float(studentExamScore))
            print(f"\n\tID: \t\t\t{studentId} \n\tName: \t\t\t{studentLastName.capitalize()}, {studentFirstName.capitalize()} \n\tClass Standing: \t{studentClassStanding} \n\tExam Score: \t\t{studentExamScore} \n\tGrade: \t\t\t{studentGrade}")
            found = True
            break
    
    if not found:
        print(f"No record found for Student ID: {studentID}")
    
    continuePrompt("show another record")
    
#######NOTES: After adding record always remember to save it in either option 2 & 3 in the main menu       
def addRecord():
    clearScreen()
    # Ask user for student details
    while True:
        studentId = input("Enter Student ID (6-digit number): ")
        if studentId.isdigit() and len(studentId) == 6:
            if studentId not in [record[0] for record in studentRecords]:
                break
            else:
                print("Student ID already exists. Please enter a unique 6-digit number.")
        else:
            print("Invalid input. Please enter a 6-digit number.")
    
    while True:
        studentLastName = input("Enter Last Name: ").strip()
        if all(part.isalpha() for part in studentLastName.split()):
            break
        else:
            print("Invalid input. Please enter a valid last name (letters and spaces only).")
            
    while True:
        studentFirstName = input("Enter First Name: ")
        if all(part.isalpha() for part in studentFirstName.split()):
            break
        else:
            print("Invalid input. Please enter a valid first name (letters and spaces only).")
    
    while True:
        studentClassStanding = input("Enter Class Standing (0-100): ")
        if studentClassStanding.isdigit() and 0 <= int(studentClassStanding) <= 100:
            break
        else:
            print("Invalid input. Please enter a grade between 0 and 100.")
            
    while True:
        studentExamScore = input("Enter Exam Score (0-100): ")
        if studentExamScore.isdigit() and 0 <= int(studentExamScore) <= 100:
            break
        else:
            print("Invalid input. Please enter an exam score between 0 and 100.")
    
    studentRecords.append((studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore))
    print("Student Record Added Successfully!")
    
    continuePrompt("add another record")
    
#######NOTES: After editing a record it will automatically be saved in the file where it was edited.
#######NOTES: You cannot edit the student ID
def editRecord():
    clearScreen()
    print(f"Showing records from file: {currentFile}")
    
    # Find a specific student based on their student ID
    studentID = input("Input Student ID to Edit: ")
    found = False
    
    for i, record in enumerate(student_records):
        if record[0] == studentID:
            studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
            print(f"Current Record: ID: {studentId}, Name: {studentLastName.capitalize()}, {studentFirstName.capitalize()}, Class Standing: {studentClassStanding}, Exam Score: {studentExamScore}")
            
            # Edit student details
            while True:
                newLastName = input(f"Enter New Last Name (current: {studentLastName}): ").strip()
                if all(part.isalpha() for part in newLastName.split()):
                    break
                else:
                    print("Invalid input. Please enter a valid last name (letters and spaces only).")
                    
            while True:
                newFirstName = input(f"Enter New First Name (current: {studentFirstName}): ").strip()
                if all(part.isalpha() for part in newFirstName.split()):
                    break
                else:
                    print("Invalid input. Please enter a valid first name (letters and spaces only).")
            
            while True:
                newClassStanding = input(f"Enter New Class Standing (current: {studentClassStanding}, 0-100): ")
                if newClassStanding.isdigit() and 0 <= int(newClassStanding) <= 100:
                    break
                else:
                    print("Invalid input. Please enter a grade between 0 and 100.")
                    
            while True:
                newExamScore = input(f"Enter New Exam Score (current: {studentExamScore}, 0-100): ")
                if newExamScore.isdigit() and 0 <= int(newExamScore) <= 100:
                    break
                else:
                    print("Invalid input. Please enter an exam score between 0 and 100.")
            
            # Update the record
            student_records[i] = (studentId, (newLastName, newFirstName), newClassStanding, newExamScore)
            print("Student Record Updated Successfully!")
            found = True
            break
    
    if not found:
        print(f"No record found for Student ID: {studentID}")
    else:
        with open(currentFile, "w+") as file:
            for record in student_records:
                studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
                file.write(f"{studentId},{studentLastName},{studentFirstName},{studentClassStanding},{studentExamScore}\n")
        print(f"Changes saved to file: {currentFile}")
    
    continuePrompt("edit another record")

#######NOTES: After editing a record it will automatically be saved in the file where it was edited.
def deleteRecord():
    clearScreen()
    print(f"Showing records from file: {currentFile}")
    
    # Find a specific student based on their student ID
    studentID = input("Input Student ID to Delete: ")
    found = False
    
    for i, record in enumerate(student_records):
        if record[0] == studentID:
            studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
            studentGrade = calcGrade(float(studentClassStanding), float(studentExamScore))
            print(f"Record to Delete: \n\tID: \t\t\t{studentId} \n\tName: \t\t\t{studentLastName.capitalize()}, {studentFirstName.capitalize()} \n\tClass Standing: \t{studentClassStanding} \n\tExam Score: \t\t{studentExamScore} \n\tGrade: \t\t\t{studentGrade}")
            
            confirm = input("Are you sure you want to delete this record? (y/n): ").strip().lower()
            if confirm == 'y':
                del student_records[i]
                print("Student Record Deleted Successfully!")
                found = True
            else:
                print("Deletion Cancelled.")
            break
    
    if not found:
        print(f"No record found for Student ID: {studentID}")
    else:
        with open(currentFile, "w+") as file:
            for record in student_records:
                studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore = record
                file.write(f"{studentId},{studentLastName},{studentFirstName},{studentClassStanding},{studentExamScore}\n")
        print(f"Changes saved to file: {currentFile}")
    
    continuePrompt("delete another record")
        
if __name__ == "__main__":
    main_menu()
    
