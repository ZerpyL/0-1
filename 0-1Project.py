
# List of authorized vehicles
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

# Loop to always show the menu until the user chooses to exit
while True:
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# Ask the user to choose an option
    choice = input("Enter your choice: ")

# If user chooses 1 then it lists authorized vehicles
    if choice == "1":
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for v in AllowedVehiclesList:
            print(v)
 # if user chooses 2 then exit the program           
    elif choice == "2":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        input("Press Enter to exit...")
        break
# If the user enters anything else, let them know it's invalid
    else:
        print("Invalid choice.")