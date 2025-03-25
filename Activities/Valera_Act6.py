#Author: Valera, Tamiyah Gale
#Date: 25/03/2025

import os

class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id} \nName: {self.name} \nDescription: {self.description} \nPrice: PHP{self.price:.2f}"

class ItemCRUD:
    def __init__(self):
        self.items = []
        self.load_items()

    def load_items(self):
        file_path = os.path.join(os.path.dirname(__file__), "items.txt")
        # Ensure the file exists
        if not os.path.exists(file_path):
            open(file_path, "w").close()  # Create an empty file if it doesn't exist
        else:
            with open(file_path, "r") as file:
                for line in file:
                    item_id, name, description, price = line.strip().split(",")
                    item_id = int(item_id)
                    price = float(price)
                    item = Item(item_id, name, description, price)
                    self.items.append(item)
                    
    def save_items(self):
        file_path = os.path.join(os.path.dirname(__file__), "items.txt")
        with open(file_path, "w") as file:
            for item in self.items:
                file.write(f"{item.item_id},{item.name},{item.description},{item.price:.2f}\n")
    
    def create_item(self):
        while True:
            try:
                # Input and validate item_id
                while True:
                    try:
                        item_id = int(input("Enter Item ID: "))
                        if item_id <= 0:
                            raise ValueError("Item ID must be a positive integer.")
                        if any(item.item_id == item_id for item in self.items):
                            raise ValueError("Item ID already exists.")
                        break
                    except ValueError as ve:
                        print(f"Error: {ve}")
    
                # Input and validate name
                while True:
                    try:
                        name = input("Enter Name: ").strip()
                        if not name:
                            raise ValueError("Name cannot be empty or whitespace.")
                        break
                    except ValueError as ve:
                        print(f"Error: {ve}")
    
                # Input and validate description
                while True:
                    try:
                        description = input("Enter Description: ").strip()
                        if not description:
                            raise ValueError("Description cannot be empty or whitespace.")
                        break
                    except ValueError as ve:
                        print(f"Error: {ve}")
    
                # Input and validate price
                while True:
                    try:
                        price = float(input("Enter Price: "))
                        if price <= 0:
                            raise ValueError("Price must be a positive number.")
                        break
                    except ValueError as ve:
                        print(f"Error: {ve}")
    
                # Create and add the item
                item = Item(item_id, name, description, price)
                self.items.append(item)
                self.save_items()
                print(f"Item {item_id} created successfully.")
                return
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def read_item(self, item_id):
        while True:
            for item in self.items:
                if item.item_id == item_id:
                    return item
            raise ValueError("Item not found.")

    def update_item(self, item_id):
        while True:
            try:
                # Check if the item exists
                for item in self.items:
                    if item.item_id == item_id:
                        print(f"Updating Item: {item}")
                        
                        # Prompt for new values
                        while True:
                            try:
                                name = input("Enter Name: ").strip()
                                if not name:
                                    raise ValueError("Name cannot be empty or whitespace.")
                                break
                            except ValueError as ve:
                                print(f"Error: {ve}")
                        
                        while True:
                            try:
                                description = input("Enter Description: ").strip()
                                if not description:
                                    raise ValueError("Description cannot be empty or whitespace.")
                                break
                            except ValueError as ve:
                                print(f"Error: {ve}")
                        
                        while True:
                            try:
                                price = float(input("Enter Price: "))
                                if price <= 0:
                                    raise ValueError("Price must be a positive number.")
                                break
                            except ValueError as ve:
                                print(f"Error: {ve}")
                                
                        self.save_items()
                        print(f"Item {item_id} updated successfully.")
                        return
                
                # If item not found
                raise ValueError("Item not found.")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def delete_item(self, item_id):
        while  True:
            for item in self.items:
                if item.item_id == item_id:
                    self.items.remove(item)
                    self.save_items()
                    print(f"Item {item_id} deleted.")
                    return
            raise ValueError("Item not found.")

def main_menu():
    manager = ItemCRUD()
    
    while True:
        print('\n**********************************************')
        print("\tITEM MANAGEMENT APPLICATION")
        print('**********************************************\n')
        print("[C] Create Item")
        print("[R] Read Item")
        print("[U] Update Item")
        print("[D] Delete Item")
        print("[Q] Quit\n")
        print('**********************************************\n')
        
        try:
            choice = input("Enter Choice: ")
            if choice.lower() == "c":
                manager.create_item()
                
            elif choice.lower() == "r":
                item_id = int(input("Enter Item ID: "))
                item = manager.read_item(item_id)
                print(item)
                
            elif choice.lower() == "u":
                item_id = int(input("Enter Item ID: "))
                manager.update_item(item_id)
                
            elif choice.lower() == "d":
                item_id = int(input("Enter Item ID: "))
                manager.delete_item(item_id)
            
            elif choice.lower() == "q":
                print("Thank you for using the Item Management Application.")
                break
            else:
                print("Invalid Choice. Please Try Again!!!")
                
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()