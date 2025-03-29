#Author: Valera, Tamiyah Gale C.
#Date: 29/03/2025
#Description: Final Project for Python Programming
# This program is a simple student registration system using Tkinter for GUI and JSON for data storage.
# It allows users to sign up, view all students, and search for a student by last name.

#Important Libraries
import tkinter as tk #library used to create the GUI
import json #json also known as JavaScript Object Notation used to store data in a structured format
import os #library used to interact with the operating system
import datetime #library used to work with dates and times

# File for data persistence. This file will be used to store the student records in JSON format
DATA_FILE = "students.json" 


# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump([], file)

# Create a custom message box function that will pop up to display feedback messages to the user       
def custom_messagebox(parent, title, message):
    custom_box = tk.Toplevel(parent)
    custom_box.title(title)
    custom_box.configure(bg="black")
    tk.Label(
        custom_box, text=message, font=("Consolas", 10), fg="white", bg="black", wraplength=400
    ).pack(padx=20, pady=20)
    tk.Button(
        custom_box, text="OK", command=custom_box.destroy, fg="white", bg="black"
    ).pack(pady=10)

# Load existing records
def load_records():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save records to file
def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except Exception as e:
        custom_messagebox(app.root,"Error", f"Failed to save records: {e}")

# Main application class
class TamiyahsPythonClassApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamiyah's Python Class") # Title of the window
        self.records = load_records()
        
        # Set up the main window
        self.root.configure(bg="black") # Background color
        self.root.geometry("450x450") #the size of the window
        self.root.resizable(True, True) # Allow resizing
        
        # Configure grid weights for resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Main menu
        self.menu_frame = tk.Frame(root)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.menu_frame.configure(bg="black")
        
        # Center the menu frame in the window
        self.menu_frame.grid_rowconfigure(0, weight=1)
        self.menu_frame.grid_rowconfigure(5, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(1, weight=1)
        
        #Title of the Main Menu
        tk.Label(
            self.menu_frame,
            text="Tamiyah's Python Class \nRegistration",
            font=("Consolas", 15),
            fg="White",
            bg="black",  # Background color
            width=30,    # Width of the label
            height=2     # Height of the label
        ).grid(row=0, column=0, columnspan=1,padx=50, pady=10, sticky="ew")
        
        #Button 1 - Sign Up Form
        tk.Button(
            self.menu_frame,
            text="Sign Up",
            width=25,    # Width of the button
            height=2,    # Height of the button
            command=self.show_signup_form,
            fg="black",
            bg="#1E90FF"    # Background color of the button
        ).grid(row=2, column=0, columnspan=2, pady=5, padx=120, sticky="ew")
        
        #Button 2 - View All Students
        tk.Button(
            self.menu_frame,
            text="View All Students",
            width=25,
            height=2,
            command=self.view_all_students,
            fg="black",
            bg="#32CD32"
        ).grid(row=3, column=0, columnspan=2, pady=5, padx=120, sticky="ew")
        
        #Button 3 - Search a Student
        tk.Button(
            self.menu_frame,
            text="Search a Student",
            width=25,
            height=2,
            command=self.search_student,
            fg="black",
            bg="#FFD700"
        ).grid(row=4, column=0, columnspan=2, pady=5, padx=120, sticky="ew")
        
        #Button 4 - Exit
        tk.Button(
            self.menu_frame,
            text="Exit",
            width=25,
            height=2,
            command=self.root.quit,
            fg="black",
            bg="#FF4500"
        ).grid(row=5, column=0, columnspan=2, pady=5, padx=120, sticky="ew")

    # Show sign-up form
    def show_signup_form(self):
        self.clear_frame()
        
        # Title Label
        tk.Label(
            self.root,
            text="Sign-Up Form",
            font=("Consolas", 15),
            fg="White",
            bg="black",  # Background color
            width=30,
            height=2
        ).grid(row=0, column=0, columnspan=2, padx=22, pady=10, sticky="ew")
    
        # Input fields
        fields = ["First Name", "Middle Name", "Last Name", "Birthday (YYYY-MM-DD)"]
        self.entries = {}
        for i, field in enumerate(fields):
            # Field Label
            tk.Label(
                self.root,
                text=field,
                font=("Consolas", 10),
                fg="White",
                bg="black"
            ).grid(row=i + 1, column=0, padx=10, pady=22, sticky="w")
            
            # Entry Widget or the area where users can input their answer in the field
            entry = tk.Entry(self.root, width=35, font=("Consolas", 10))
            entry.grid(row=i + 1, column=1, padx=15, pady=22, sticky="w")
            self.entries[field] = entry
        
        # Gender Dropdown Label
        tk.Label(
            self.root,
            text="Gender",
            font=("Consolas", 10),
            fg="White",
            bg="black"
        ).grid(row=len(fields) + 1, column=0, padx=10, pady=22, sticky="w")

        # Dropdown menu for gender
        self.gender_var = tk.StringVar(self.root)
        self.gender_var.set("Select Gender")  # Default value
        gender_dropdown = tk.OptionMenu(self.root, self.gender_var, "Male", "Female", "Other")
        gender_dropdown.config(width=30, font=("Consolas", 10))
        gender_dropdown.grid(row=len(fields) + 1, column=1, padx=10, pady=22, sticky="w")
    
        # Submit Button
        tk.Button(
            self.root,
            text="Submit",
            command=self.save_student,
            fg="black",
            bg="#32CD32",
            width=15
        ).grid(row=len(fields) + 2, column=0, columnspan=2, pady=22, padx=10, sticky="e")
    
        # Back to Menu Button
        tk.Button(
            self.root,
            text="Back to Menu",
            command=self.show_menu,
            fg="black",
            bg="#FF4500",
            width=15
        ).grid(row=len(fields) + 2, column=1,columnspan=2, pady=22, padx=10, sticky="w")

    # Save student record
    def save_student(self):
        try:
            # Retrieve and validate the birthday
            birthday = self.entries["Birthday (YYYY-MM-DD)"].get().strip()
            try:
                # Check if the birthday is in the correct format
                datetime.datetime.strptime(birthday, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid Birthday. Please use the format YYYY-MM-DD.")

            # Create the student dictionary
            student = {
                "First Name": self.entries["First Name"].get().strip(),
                "Middle Name": self.entries["Middle Name"].get().strip(),
                "Last Name": self.entries["Last Name"].get().strip(),
                "Birthday": birthday,
                "Gender": self.gender_var.get().strip()
            }

            # Validate to make sure that all the fields except for middle name is not empty
            if not student["First Name"] or not student["Last Name"] or not student["Birthday"] or student["Gender"] == "Select Gender":
                raise ValueError("First Name, Last Name, Birthday, and Gender are required fields.")
            
            #If the validation is successful, the student record will be saved to the JSON file
            self.records.append(student)
            save_records(self.records)
            custom_messagebox(self.root,"Success", "Student record saved successfully!")
            
        # Handle specific exceptions and display custom error messages
        except ValueError as ve: 
            custom_messagebox(self.root,"Error", str(ve))
        except Exception as e:
            custom_messagebox(self.root,"Error", f"An unexpected error occurred: {e}")

    # View all students
    def view_all_students(self):
        self.clear_frame()

        # Title Label
        tk.Label(
            self.root,
            text="All Students",
            font=("Consolas", 15),
            fg="White",
            bg="black", 
            width=30,
            height=1
        ).grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        if not self.records:
            # Display message if no records are found
            tk.Label(
                self.root,
                text="No records found.",
                font=("Consolas", 12),
                fg="White",
                bg="black"
            ).grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")
            
        else:
            # Sorting options
            sort_frame = tk.Frame(self.root, bg="black")
            sort_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

            tk.Label(
                sort_frame,
                text="Sort by Last Name:",
                font=("Consolas", 10),
                fg="White",
                bg="black"
            ).grid(row=0, column=0, padx=5, columnspan=1, pady=20, sticky="ew")

            tk.Button(
                sort_frame,
                text="Ascending",
                command=lambda: self.display_students(sorted(self.records, key=lambda x: x['Last Name'])),
                fg="black",
                bg="#32CD32"
            ).grid(row=0, column=1, padx=5, columnspan=1, pady=20, sticky="w")

            tk.Button(
                sort_frame,
                text="Descending",
                command=lambda: self.display_students(sorted(self.records, key=lambda x: x['Last Name'], reverse=True)),
                fg="black",
                bg="#FF4500"
            ).grid(row=0, column=2, padx=5, columnspan=1, pady=20, sticky="ew")

            # Display students initially unsorted
            self.display_students(self.records)

            # Back to Menu Button
            tk.Button(
                self.root,
                text="Back to Menu",
                command=self.show_menu,
                fg="black",
                bg="#FF4500",
                width=15
            ).grid(row=4, column=0, columnspan=2, pady=20,padx=150, sticky="ew")

    # Helper method to display students
    def display_students(self, students):
        # Create a frame for student information
        student_frame = tk.Frame(self.root, bg="black")
        student_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Start displaying students from row 0 in the student_frame
        for i, student in enumerate(students):
            student_info = f" {student['Last Name']}, {student['First Name']} {student['Middle Name']} - {student['Birthday']} - {student['Gender']}"
            tk.Label(
                student_frame,
                text=student_info,
                font=("Consolas", 10),
                fg="White",
                bg="black"
            ).grid(row=i, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

   # Search for a student
    def search_student(self):
        self.clear_frame()

        # Title Label
        tk.Label(
            self.root,
            text="Search a Student",
            font=("Consolas", 15),
            fg="White",
            bg="black",
            width=30,
            height=1
        ).grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Search input field
        tk.Label(
            self.root,
            text="Enter Last Name:",
            font=("Consolas", 10),
            fg="White",
            bg="black"
        ).grid(row=1, column=0, padx=20, pady=15, sticky="e")

        self.search_entry = tk.Entry(self.root, width=20, font=("Consolas", 10))
        self.search_entry.grid(row=2, column=0, columnspan=2, padx=50, pady=15, sticky="ew")

        # Search button
        tk.Button(
            self.root,
            text="Search",
            command=self.perform_search,
            fg="black",
            bg="#32CD32",
            width=15
        ).grid(row=3, column=0, pady=20, padx=20, sticky="e")

        # Back to Menu button
        tk.Button(
            self.root,
            text="Back to Menu",
            command=self.show_menu,
            fg="black",
            bg="#FF4500",
            width=15
        ).grid(row=3, column=1, pady=20, padx=20, sticky="w")

    # Perform search
    def perform_search(self):
        query = self.search_entry.get().strip()
        results = [student for student in self.records if student["Last Name"].lower() == query.lower()] # Case insensitive search but if there is a student with the same last name, they will be displayed in the search results

        if results:
            result_text = "\n".join(
                f"{student['First Name']} {student['Middle Name']} {student['Last Name']} - {student['Birthday']} - {student['Gender']}"
                for student in results
            )
            custom_messagebox(self.root,"Search Results", result_text)
        else:
            custom_messagebox(self.root, "Search Results", "No matching records found.")

    # Show main menu
    def show_menu(self):
        self.clear_frame()
        self.__init__(self.root)

    # Clear current frame
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TamiyahsPythonClassApp(root)
    root.mainloop() #open the window and start the application
# The code is complete and will run a simple student registration system with a GUI.