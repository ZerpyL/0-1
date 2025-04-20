import os

# Constants
VEHICLE_FILE = "allowed_vehicles.txt" 

# Loads vehicles from the file or creates a default list if the file does not exist
def load_vehicles():
    if not os.path.exists(VEHICLE_FILE):
        default_vehicles = [
            'Ford F-150', 
            'Chevrolet Silverado', 
            'Tesla CyberTruck',
            'Toyota Tundra', 
            'Rivian R1T', 
            'Ram 1500'
        ]
        with open(VEHICLE_FILE, 'w') as f:
            f.write('\n'.join(default_vehicles))
        return default_vehicles
    
    with open(VEHICLE_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Saves the current vehicles list
def save_vehicles(vehicles):
    with open(VEHICLE_FILE, 'w') as f:
        f.write('\n'.join(vehicles))

# Dsiplays the main menu for the users inputs
def display_menu():
    """Display the main program menu"""
    print("********************************")
    print("AutoCountry Vehicle Finder v1.0")
    print("********************************")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

# Dsiplays all the authorized vehicles in a list
def display_all_vehicles(vehicles):
    print("The AutoCountry sales manager has authorized the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)

# Prompts the user for their choice 
def get_user_choice():
    return input("Enter your choice (1-5): ").strip()

# Gives user a choice to search for if a vehicle is on the authorized vehicles list 
def search_vehicle(vehicles):
    search_term = input("Enter full Vehicle name: ").strip()
    if search_term in vehicles:
        print(f"{search_term} is authorized")
    else:
        print(f"{search_term} not authorized - check spelling")

# Gives user a choice to add a new vehicle to the authorized vehicles list 
def add_vehicle(vehicles):
    new_vehicle = input("Enter full Vehicle name to add: ").strip()
    if new_vehicle in vehicles:
        print(f"{new_vehicle} already exists")
        return vehicles
        
    vehicles.append(new_vehicle)
    save_vehicles(vehicles)
    print(f"Added {new_vehicle} to authorized vehicles")
    return vehicles
# Gives user a choice to remove a vehicle from the authorized vehicles list
def delete_vehicle(vehicles):
    vehicle = input("Enter full Vehicle name to remove: ").strip()
    if vehicle not in vehicles:
        print(f"{vehicle} not found")
        return vehicles
        
    confirm = input(f"Confirm removal of {vehicle}? (yes/no): ").lower()
    if confirm == 'yes':
        vehicles.remove(vehicle)
        save_vehicles(vehicles)
        print(f"Removed {vehicle} from authorized vehicles")
    else:
        print("Cancelled removal")
    
    return vehicles

# Main function to run the pogram by prompting the user based on their input
def main():
    vehicles = load_vehicles()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            display_all_vehicles(vehicles)
        elif choice == "2":
            search_vehicle(vehicles)
        elif choice == "3":
            vehicles = add_vehicle(vehicles)
        elif choice == "4":
            vehicles = delete_vehicle(vehicles)
        elif choice == "5":
            print("Thank you for using AutoCountry Vehicle Finder!")
            input("Press Enter to exit...")
            break
        else:
            print("Invalid choice - please enter 1-5")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()