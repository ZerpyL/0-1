import os

# Constants
VEHICLE_FILE = "allowed_vehicles.txt"

# Loads vehicles from the file or creates a default file if it does not exist
def load_vehicles():
    """Load vehicles from file or create default if file doesn't exist"""
    if not os.path.exists(VEHICLE_FILE):
        # Create file with default vehicles
        default_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']
        with open(VEHICLE_FILE, 'w') as f:
            for vehicle in default_vehicles:
                f.write(vehicle + '\n')
        return default_vehicles
    else:
        # Read vehicles from file
        with open(VEHICLE_FILE, 'r') as f:
            return [line.strip() for line in f.readlines() if line.strip()]

# Saves the current vehicles list
def save_vehicles(vehicles):
    """Save vehicles to file"""
    with open(VEHICLE_FILE, 'w') as f:
        for vehicle in vehicles:
            f.write(vehicle + '\n')

# Displays the main menu to the user for the users inputs
def print_menu():
    """Print the program menu"""
    print("********************************")
    print("AutoCountry Vehicle Finder 0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

# Handles the core functionality of the program
def main():
    AllowedVehiclesList = load_vehicles()

# Main Program Loop
    while True:
        # Display for the users inputs
        print_menu()
        choice = input("Enter your choice: ")

        # Prints all authorized vehicles from the list when the user selects 1
        if choice == "1":
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for v in AllowedVehiclesList:
                print(v)
        # Searches for if a vehicle is on the authorized vehicles list when the user selects 2
        elif choice == "2":
            search_vehicle = input("Please enter the full Vehicle name: ")
            if search_vehicle in AllowedVehiclesList:
                print(f"{search_vehicle} is an authorized vehicle")
            else:
                print(f"{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")
        # Adds a new vehicle to the authorized vehicles list when the user selects 3
        elif choice == "3":
            new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
            if new_vehicle not in AllowedVehiclesList:
                AllowedVehiclesList.append(new_vehicle)
                save_vehicles(AllowedVehiclesList)
                print(f'You have added "{new_vehicle}" as an authorized vehicle')
            else:
                print(f'"{new_vehicle}" is already in the authorized vehicles list')
        # Deletes a vehicle from the authorized vehicles list when the user selects 4
        elif choice == "4":
            remove_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
            if remove_vehicle in AllowedVehiclesList:
                confirmation = input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ')
                if confirmation.lower() == 'yes':
                    AllowedVehiclesList.remove(remove_vehicle)
                    save_vehicles(AllowedVehiclesList)
                    print(f'You have REMOVED "{remove_vehicle}" as an authorized vehicle')
                else:
                    print("Vehicle removal canceled.")
            else:
                print(f'"{remove_vehicle}" was not found in the authorized vehicles list')
        # Exits the program when the user selects 5 
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            input("Press Enter to exit...")
            break
        # Handles invalid input from the user
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()