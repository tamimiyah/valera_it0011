# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-23

import csv
import os

###### PART 1. SET

def Set():
    A = {"a","b","c","d","e","f","g"}
    B = {"b","c","h","l","m","o"} 
    C = {"c","d","f","h","j","i","k"}
    
    print(f"Set A = {A}")
    print(f"Set B = {B}")
    print(f"Set C = {C}")
    
    #How many elements are there in Set A and B?
    unionAB = A.union(B)
    countAB = len(unionAB)
    print("\n# of Elements in A and B: ", countAB)
    
    #How many elements are there in B that is not part of A and C
    BMinusAC = B - (A.union(C))
    countBMinusAC = len(BMinusAC)
    print("\n# of Elements in B that is not part of A and C: ", countBMinusAC)
    
    # Show [h, i, j, k]
    showHIJK = C - A
    print("\n", showHIJK)
    
    # Show [c, d, f]
    intersectionAC = A.intersection(C)
    print("\n", intersectionAC) 
    
    # Show [b, c, h]
    unionAC = A.union(C)
    showBCH = B & unionAC
    print("\n", showBCH) 
    
    # Show [d, f]
    showDF = (A & C) - B
    print("\n", showDF) 
    
    # Show [c] - Intersect A,B, and C
    showC = A & B & C
    print("\n", showC)
    
    # Show [l, m, o]
    print("\n", BMinusAC)
    
###### PART 2. DICTIONARY
def Dictio():
    file_path = os.path.join(os.path.dirname(__file__), "currency.csv")
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        exchange = {row["code"]:float(row["rate"]) for row in reader}
    
    # Double checking if the cvs file was imported properly
    # for d in exchange:
    #     print(d)
    
    try:
        dollars = float(input("How much dollar do you have? "))
        currency = input("What currency do you want to have? ").upper()
        
        if currency in exchange:
            converted_amount = dollars * exchange[currency]
            print(f"\nDollar: {dollars} USD")
            print(f"Converted to {currency}: {converted_amount:.2f} {currency}")
        else:
            print(f"Currency '{currency}' not found in the exchange rates.")
    except ValueError:
        print("Invalid input. Please enter a valid number for dollars.")
    
    
    

def main_menu():
    
    while True:
        print("\nChoose A Part:")
        print("1. Set")
        print("2. Dictionary")
        print("3. Exit")
        
        choice = input("Part: ")
        if choice == "1":
            Set()
        if choice =="2":
            Dictio()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid Choice. Please Try Again!!!")
            
        
        
        
if __name__ == "__main__":
    main_menu()