""" Importing the required functions from write.py and operations.py"""
from write import display_laptops
from operations import laptop_purchase, laptop_sales

print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  WELCOME TO NICE LAPTOP SHOP\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Putalisadak, Kathmandu\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Contact no : 4381923\n\n")

display_laptops()  # Calling display_laptops function to display details of laptop
while True:
    print("\n\nSelect any option?\n")
    print("Press 1 : LAPTOP SALES TO CUSTOMER")
    print("Press 2 : LAPTOP PURCHASE FROM MANUFACTURER")
    print("Press 3 : EXIT FROM SYSTEM")

    choice = input("\n--> ")

    if choice == '1':
        laptop_sales()  # Calling laptop_sales() function

    elif choice == '2':
        laptop_purchase()  # Calling laptop_purchase() function

    elif choice == '3':
        break  # exit from loop and end the program

    else:
        print("Enter valid input\n")
