# AUTHOR: Valera, Tamiyah Gale C.
# DATE: 2025-03-24

def div():
    while True:
        try:
            num1 = int(input("Enter 1st Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        try:
            num2 = int(input("Enter 2nd Number: "))
            if num2 != 0:
                break
            else:
                print("2nd Number Must Not Be Equal to 0")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    quotient = float(num1 / num2)
    print("Quotient: {:.4f}".format(quotient))
    
def exp():
    while True:
        try:
            num1 = int(input("Enter 1st Number(base): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        try:
            num2 = int(input("Enter 2nd Number(exponent): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    power = pow(num1,num2)
    
    print("Power: ", power)

def rem():
    while True:
        try:
            num1 = int(input("Enter 1st Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        try:
            num2 = int(input("Enter 2nd Number: "))
            if num2 != 0:
                break
            else:
                print("2nd Number Must Not Be Equal to 0")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    remainder = num1 % num2
    print("Remainder: ", remainder) 
    

def summ():
    while True:
        try:
            num1 = int(input("Enter 1st Number(start): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        try:
            num2 = int(input("Enter 2nd Number(end): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        if num2 > num1:
            break
        else:
            print("2nd number must be greater than the 1st number")
            
    total = sum(range(num1, num2 + 1))
    print("Summation: ", total)
    
        
            
if __name__ == "__main__":
    while True:
        print("\n\n******************************************************")
        print("\tMathematical Operations to Perform")
        print("******************************************************")
        print("[D] Divide")
        print("[E] Exponentiation")
        print("[R] Remainder")
        print("[F] Summation")
        print("[X] Exit")
    
        choice = input("\nEnter Choice: ").strip().lower()
    
        if choice == "d":
            div()
        elif choice == "e":
            exp()
        elif choice == "r":
            rem()
        elif choice == "f":
            summ()
        elif choice == "x":
            break
        else:
            print("Invalid Choice. Try Again")