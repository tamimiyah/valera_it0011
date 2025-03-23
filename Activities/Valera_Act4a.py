# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-23

import os

# Global variable to store student records
student_records = []

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def calcGrade(studentClassStanding, studentExamScore):
    return (0.6 * studentClassStanding) + (0.4 * studentExamScore)

def main_menu():
    clearScreen()
    while True:
        print("\n******************************************************************************")
        print("\t\tSTUDENT MANAGEMENT SYSTEM")
        print("******************************************************************************")
        print("\n1. Open File")
        print("2. Save File")
        print("3. Save as File")
        print("4. Show All Students Record")
        print("5. Show a Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == "1":
            openFile()
        elif choice == 2:
            saveFile()
        # elif choice == 3:
        #     saveAsFile()
        #elif choice == 4:
            #showAllRecords()
        #elif choice == 5:
            #showRecord()
        elif choice == "6":
            addRecord()
        # elif choice == 7:
        #     editRecord()
        # elif choice == 8:
        #     deleteRecord()
        elif choice == "9":
            print("Exiting Program....")
            break
        else:
            print("Invalid Choice. Please Try Again!!!")
               
def openFile():
    clearScreen()
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
        print(f"File '{fileName}' loaded successfully!")
    else:
        print(f"File '{fileName}' does not exist.")
    while True:
        choice = input("Do you want to open another file? (y/n): ").strip().lower()
        if choice == 'y':
            openFile()
            break
        elif choice == 'n':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
def saveFile():
    clearScreen()
    fileName = input("Enter the Filename to save: ")
            
    
def addRecord():
    clearScreen()
    # Ask user for student details
    while True:
        studentId = input("Enter Student ID (6-digit number): ")
        if studentId.isdigit() and len(studentId) == 6:
            if studentId not in [record[0] for record in student_records]:
                break
            else:
                print("Student ID already exists. Please enter a unique 6-digit number.")
        else:
            print("Invalid input. Please enter a 6-digit number.")
    
    while True:
        studentLastName = input("Enter Last Name: ")
        if studentLastName.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid last name.")
            
    while True:
        studentFirstName = input("Enter First Name: ")
        if studentFirstName.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid first name.")
    
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
    
    student_records.append((studentId, (studentLastName, studentFirstName), studentClassStanding, studentExamScore))
    print("Student Record Added Successfully!")
    
    while True:
        choice = input("Do You Want to Add Record? (y/n)").strip().lower()
        if choice == 'y':
            addRecord()
            break
        elif choice == 'n':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
if __name__ == "__main__":
    main_menu()