# Portfolio Building
# By Vinson Leo Veronal Jong
# Membuat Aplikasi CRUD
# Cargo Systems Management

# Import Library For The Table
from tabulate import tabulate

# Nested Dictionary For Vehicles List
vehicles = {
    1 : 
        {"name": "Car", 
         "capacity": 1000, 
         "status": "Available"
        },
    2 : {
        "name": "SUV", 
        "capacity": 2000, 
        "status": "Available"
        },
    3 : {
        "name": "Van", 
        "capacity": 2500, 
        "status": "Available"
        },
    4 : {
        "name": "Pickup", 
        "capacity": 2950, 
        "status": "Available"
        },
    5: {
        "name": "Truck", 
        "capacity": 5000, 
        "status": "Available"
        }
}

# Nested Dictionary For Cargo List
cargo_list = {
    1 : {
        "name": "Box 1", 
        "weight": 800, 
        "vehicle": "Car"
    },
    2 : {
        "name": "Crate 1", 
        "weight": 1500, 
        "vehicle": "SUV"
    },
    3 : {
        "name": "Parcel 1", 
        "weight": 2200, 
        "vehicle": "Van"
    }
}

def display_cargo():
    cargo_data = []
    for cargo_id, cargo in cargo_list.items():
        cargo_data.append({"id": cargo_id, "name": cargo["name"], "weight": cargo["weight"], "vehicle": cargo["vehicle"]})
    print(tabulate(cargo_data, headers="keys", tablefmt="outline", intfmt = ","))

def display_vehicles():
    vehicles_data = []
    for vehicle_id, vehicle in vehicles.items():
        vehicles_data.append({"id": vehicle_id, "name": vehicle["name"], "capacity": vehicle["capacity"], "status": vehicle["status"]})
    print(tabulate(vehicles_data, headers="keys", tablefmt="outline", intfmt = ","))

def add_cargo():
    name = input("Enter cargo name: ")
    weight = float(input("Enter cargo weight (kg): "))
    suitable_vehicles = []
    
    for vehicle_id, vehicle in vehicles.items():
        if vehicle["capacity"] >= weight and vehicle["status"] == "Available":
            suitable_vehicles.append(vehicle_id)
            
    if not suitable_vehicles:
        print("No available vehicle can carry this cargo.")
        return
    
    while True:
        print("\nAvailable Vehicles:")
        display_vehicles()
        vehicle_id = int(input("Enter the ID of the vehicle for this cargo: "))
        
        if vehicle_id in vehicles:
            selected_vehicle = vehicles[vehicle_id]
            if selected_vehicle["capacity"] >= weight:
                break
            else:
                print("Selected vehicle cannot carry this cargo. Please choose another vehicle.")
        else:
            print("Invalid vehicle ID. Please select a valid option.")
    
    vehicle_choice = vehicle_id
    cargo_id = len(cargo_list) + 1
    cargo_list[cargo_id] = {"name": name, "weight": weight, "vehicle": vehicles[vehicle_choice]["name"]}
    vehicles[vehicle_choice]["status"] = "Not Available"
    
    print("Cargo added and assigned to vehicle successfully!")

def add_vehicle():
    name = input("Enter vehicle name: ")
    capacity = float(input("Enter vehicle capacity (kg): "))
    
    vehicle_id = len(vehicles) + 1
    vehicles[vehicle_id] = {"name": name, "capacity": capacity, "status": "Available"}
    print("Vehicle added successfully!")
    
def add_item():
    print("\nAdd Item:")
    print("1. Add Cargo:")
    print("2. Add Vehicle:")
    add_item_choice = int(input("Enter your choice: "))  # Prompt to choose what item to add
    if add_item_choice == 1:
        add_cargo()  # Call the add_cargo function
    elif add_item_choice == 2:
        add_vehicle()  # Call the add_vehicle function
    else:
        print("Invalid choice.")   
    
def update_vehicle_status(vehicle_id, status):
    vehicles[vehicle_id]["status"] = status
    
def delete_menu():
    print("\nDelete Menu:")
    print("1. Delete Cargo")
    print("2. Delete Vehicle")
    delete_choice = int(input("Enter your choice: "))
    
    if delete_choice == 1:
        cargo_id = int(input("Enter the ID of the cargo to delete: "))
        delete_cargo(cargo_id)
    elif delete_choice == 2:
        vehicle_id = int(input("Enter the ID of the vehicle to delete: "))
        delete_vehicle(vehicle_id)
    else:
        print("Invalid choice. Returning to the main menu.")


def delete_vehicle(vehicle_id):
    if vehicle_id in vehicles:
        update_vehicle_status(vehicle_id, "Available")
        
        del vehicles[vehicle_id]
        
        # Rearrange vehicle IDs after deletion
        new_vehicles = {}
        for new_id, (old_id, vehicle) in enumerate(vehicles.items(), start=0):
            new_vehicles[new_id] = vehicle
        
        vehicles.clear()
        vehicles.update(new_vehicles)
        
        print("Vehicle deleted successfully!")
    else:
        print("Invalid vehicle ID.")

def delete_cargo(cargo_id):
    if cargo_id in cargo_list:
        del cargo_list[cargo_id]
        
        # Rearrange cargo IDs after deletion
        new_cargo_list = {}
        for new_id, (old_id, cargo) in enumerate(cargo_list.items(), start=1):
            new_cargo_list[new_id] = cargo
        
        cargo_list.clear()
        cargo_list.update(new_cargo_list)
        
        print("Cargo deleted successfully!")
    else:
        print("Invalid cargo ID.")
    
def update_menu():
    print("\nUpdate Menu:")
    print("1. Update Cargo")
    print("2. Update Vehicle")
    update_choice = int(input("Enter your choice: "))
    
    if update_choice == 1:
        update_cargo()
    elif update_choice == 2:
        update_vehicle()
    else:
        print("Invalid choice. Returning to main menu.")

def update_cargo():
    print("\nUpdate Cargo:")
    display_cargo()
    while True:
        cargo_id = int(input("Enter the ID of the cargo to update: "))
        if cargo_id in range(len(cargo_list)):
            print("1. Update Cargo Name")
            print("2. Update Cargo Weight")
            cargo_update_choice = int(input("Enter your choice: "))
            if cargo_update_choice == 1:
                new_name = input("Enter new cargo name: ")
                cargo_list[cargo_id]["name"] = new_name
                print("Cargo name updated successfully!")
            elif cargo_update_choice == 2:
                new_weight = float(input("Enter new cargo weight (kg): "))
                cargo_list[cargo_id]["weight"] = new_weight
                print("Cargo weight updated successfully!")
            else:
                print("Invalid choice.")
        else:
            print("Invalid cargo ID.")
        break

def update_vehicle():
    print("\nUpdate Vehicle:")
    display_vehicles()
    while True: 
        vehicle_id = int(input("Enter the ID of the vehicle to update: "))
        if vehicle_id in vehicles:
            print("1. Update Vehicle Name")
            print("2. Update Vehicle Capacity")
            vehicle_update_choice = int(input("Enter your choice: "))
            if vehicle_update_choice == 1:
                new_name = input("Enter new vehicle name: ")
                vehicles[vehicle_id]["name"] = new_name
                print("Vehicle name updated successfully!")
            elif vehicle_update_choice == 2:
                new_capacity = input("Enter new vehicle capacity (e.g., 3000 Kg): ")
                vehicles[vehicle_id]["capacity"] = new_capacity
                print("Vehicle capacity updated successfully!")
            else:
                print("Invalid choice.")
        else:
            print("Invalid vehicle ID.")
        break

# Main Menu For The Program (loop)
while True:
    print("\n==== Kim Cargo Management Program ====")
    print("1. Display Cargo")
    print("2. Display Vehicles")
    print("3. Add Items")
    print("4. Delete Item")
    print("5. Update")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        display_cargo()
    elif choice == 2:
        display_vehicles()
    elif choice == 3:
        add_item()
    elif choice == 4:
        display_cargo()
        delete_menu()
    elif choice == 5:
        update_menu()
    elif choice == 6:
        print("Thankyou For Using Kim Cargo Management Program.")
        break
    else:
        print("Menu Not Found. Please select a valid menu.")