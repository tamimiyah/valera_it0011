import os

class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"

class ItemCRUD:
    def __init__(self):
        self.items = []
        self.load_items()

    def load_items(self):
        file_path = os.path.join(os.path.dirname(__file__), "items.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                for line in file:
                    item_id, name, description, price = line.strip().split(",")
                    item_id = int(item_id)
                    price = float(price)
                    item = Item(item_id, name, description, price)
                    self.items.append(item)

    def create_item(self, item_id, name, description, price):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if any(item.item_id == item_id for item in self.items):
            raise ValueError("Item ID already exists.")
        if not name or not name.strip():
            raise ValueError("Name cannot be empty or whitespace.")
        if not description or not description.strip():
            raise ValueError("Description cannot be empty or whitespace.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        
        item = Item(item_id, name.strip(), description.strip(), price)
        self.items.append(item)
        return item

    def read_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ValueError("Item not found.")

    def update_item(self, item_id, name, description, price):
        for item in self.items:
            if item.item_id == item_id:
                if name:
                    item.name = name
                if description:
                    item.description = description
                if price is not None:
                    if price <= 0:
                        raise ValueError("Price must be greater than zero.")
                    item.price = price
                print(f"Item {item_id} updated.")
                return
        raise ValueError("Item not found.")

    def delete_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"Item {item_id} deleted.")
                return
        raise ValueError("Item not found.")

def main_menu():
    manager = ItemCRUD()
    
    while True:
        print('\n**********************************************')
        print("\tTEM MANAGEMENT APPLICATION")
        print('**********************************************\n')
        print("[C] Create Item")
        print("[R] Read Item")
        print("[U] Update Item")
        print("[D] Delete Item")
        print("[Q] Quit")
        print('**********************************************\n')
        
        try:
            choice = input("Enter Choice: ")
            if choice.lower() == "c":
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                manager.create_item(item_id, name, description, price)
                print("Item created.")
                
            elif choice.lower() == "r":
                item_id = int(input("Enter Item ID: "))
                item = manager.read_item(item_id)
                print(item)
                
            elif choice.lower() == "u":
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                manager.update_item(item_id, name, description, price)
                
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