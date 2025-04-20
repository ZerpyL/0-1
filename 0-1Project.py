
# List of authorized vehicles
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

# Loop to always show the menu until the user chooses to exit
while True:
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

# Ask the user to choose an option
    choice = input("Enter your choice: ")

# If user chooses 1 then it lists authorized vehicles
    if choice == "1":
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for v in AllowedVehiclesList:
            print(v)
    
    # if user chooses 2 then it searches for if vehicle is in the authorized vehicle list
    elif choice == "2":
        search_vehicle = input("Please enter the full Vehicle name: ")
        
        if search_vehicle in AllowedVehiclesList:
            print(f"{search_vehicle} is an authorized vehicle")
        else:
            print(f"{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    
    # if user chooses 3 then add a new authorized vehicle
    elif choice == "3":
        new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle')
    
    # if user chooses 4 then exit the program           
    elif choice == "4":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        input("Press Enter to exit...")
        break
    
    # If the user enters anything else, let them know it's invalid and to choose again
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")