#AUTHOR: VALERA, TAMIYAH GALE C.
#DATE: 2025-02-11

#Create a program that will translate a given date format in mm/dd/yyyy to more human readable format like January 1, 2023

date = input("\nEnter a date in mm/dd/yyyy format: ")

# Split the date into month, day, and year
month, day, year = date.split('/')

# Create a list of month names
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Convert the month number to a month name
month_name = months[int(month) - 1]

# Validate the month
if not (1 <= int(month) <= 12):
    print("Invalid month. Please enter a month between 01 and 12.")
    exit()

# Validate the day
if month in ['04', '06', '09', '11']:
    if not (1 <= int(day) <= 30):
        print("Invalid day. Please enter a day between 01 and 30 for the given month.")
        exit()
elif month == '02':
    # Check for leap year
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
        if not (1 <= int(day) <= 29):
            print("Invalid day. Please enter a day between 01 and 29 for February in a leap year.")
            exit()
    else:
        if not (1 <= int(day) <= 28):
            print("Invalid day. Please enter a day between 01 and 28 for February in a non-leap year.")
            exit()
else:
    if not (1 <= int(day) <= 31):
        print("Invalid day. Please enter a day between 01 and 31 for the given month.")
        exit()

# Print the date in a more human readable format
print(f"{month_name} {int(day)}, {year}")




