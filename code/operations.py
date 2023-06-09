""" Importing the required functions from write.py and read.py"""
from read import read_laptop_list
from write import update_stock, generate_sales_invoice, generate_purchase_invoice


def id_quantity_validation_sales(laptops):
    """This function validates the laptop id and quantity entered by the user for laptop sales"""
    temp = True
    while temp:
        while True:
            print("\nEnter the ID of laptop that you want to buy : ")
            try:
                lpt_id = int(input())
                break
            except ValueError:
                print("Invalid input")

        availability = False
        for key in laptops.keys():
            if int(key) == lpt_id:
                availability = True
                lpt_name = (laptops[key])[0].rstrip()
                qty_available = int((laptops[key])[3].rstrip())

                if qty_available == 0:
                    print("This laptop is out of stock")
                    break

                while True:
                    while True:
                        try:
                            qty = int(input(f"How many {lpt_name} do you want?\n"))
                            break

                        except ValueError:
                            print("Invalid input")

                    if qty <= 0:
                        print("Please enter appropriate amount")

                    elif qty > qty_available:
                        print("The required amount of laptop is not available")

                    else:
                        temp = False
                        break

                return [lpt_id, qty]

        if not availability:
            print("The laptop of specified ID is not available in our shop")


def id_quantity_validation_purchase(laptops):
    """This function validates the laptop id and quantity entered by the user for laptop purchase"""
    temp = True
    while temp:
        while True:
            print("\nEnter the ID of laptop that you want to order : ")
            try:
                lpt_id = int(input())
                break
            except ValueError:
                print("Invalid input")

        availability = False
        for key in laptops.keys():
            if int(key) == lpt_id:
                availability = True
                lpt_name = (laptops[key])[0].rstrip()

                while True:
                    while True:
                        try:
                            qty = int(input(f"How many {lpt_name} do you want?\n"))
                            break

                        except ValueError:
                            print("Invalid input")

                    if qty <= 0:
                        print("Please enter appropriate amount of laptop")

                    else:
                        temp = False
                        break

                return [lpt_id, qty]

        if not availability:
            print("The laptop of specified ID is not available in our stock")


def laptop_sales():
    """This function is used to make laptop sales to customer"""
    flag = True
    name = input("\nEnter your name : ")
    address = input("Enter your address : ")
    while True:
        try:
            phone_no = int(input("Enter your Phone number : "))
            break

        except ValueError:
            print("Invalid input")

    users_laptop = []  # empty list declaration

    while flag:
        laptops = read_laptop_list()
        data = id_quantity_validation_sales(laptops)
        laptop_id = data[0]
        quantity = data[1]
        laptop_name = laptops[laptop_id][0].rstrip()
        brand = laptops[laptop_id][1].rstrip()
        cost = laptops[laptop_id][2].rstrip()

        kind = 'sales'
        update_stock(laptop_id, quantity, kind)  # calling update_stock function with the appropriate arguments
        users_laptop.append([laptop_id, laptop_name, brand, quantity, cost])
        print("\nThank you for purchasing our product")

        while True:
            print("\nDo you want to buy more laptops? (Type 'y' or 'Y' for yes / 'n' or 'N' for no) ")
            answer1 = input("--> ")

            if answer1 == 'y' or answer1 == 'Y':
                break

            elif answer1 == 'n' or answer1 == 'N':
                flag = False
                break

            else:
                print("Please enter appropriate response!!!")

    while True:
        print("Do you want to ship your product ? (Type 'y' or 'Y' for yes / 'n' or 'N' for no) ")
        ans = input("--> ")

        if ans == 'y' or ans == 'Y':
            shipment = True
            # calling generate_sales_invoice function with appropriate arguments
            generate_sales_invoice(name, address, phone_no, users_laptop, shipment)
            break

        elif ans == 'n' or ans == 'N':
            shipment = False
            # calling generate_sales_invoice function with appropriate arguments
            generate_sales_invoice(name, address, phone_no, users_laptop, shipment)
            break

        else:
            print("Please enter appropriate response!!!")


def laptop_purchase():
    """This function is used to order laptop from manufacturers"""
    """This function is used to make laptop sales to customer"""
    flag = True
    name = input("\nEnter your name : ")
    address = input("Enter your address : ")
    while True:
        try:
            phone_no = int(input("Enter your Phone number : "))
            break
        except ValueError:
            print("Invalid input")
    users_laptop = []  # empty list declaration
    while flag:
        laptops = read_laptop_list()
        data = id_quantity_validation_purchase(laptops)
        laptop_id1 = data[0]
        quantity1 = data[1]
        laptop_name1 = laptops[laptop_id1][0].rstrip()
        brand1 = laptops[laptop_id1][1].rstrip()
        cost1 = laptops[laptop_id1][2].rstrip()

        kind = 'purchase'
        update_stock(laptop_id1, quantity1, kind)  # calling update_stock function with the appropriate arguments
        users_laptop.append([laptop_id1, laptop_name1, brand1, quantity1, cost1])
        print("\nThank you for ordering our product")

        while True:
            print("\nDo you want to order more laptops? (Type 'y' or 'Y' for yes / 'n' or 'N' for no) ")
            answer1 = input("--> ")

            if answer1 == 'y' or answer1 == 'Y':
                break

            elif answer1 == 'n' or answer1 == 'N':
                flag = False
                break

            else:
                print("Please enter appropriate response!!!")

    # calling generate_purchase_invoice function with appropriate arguments
    generate_purchase_invoice(name, address, phone_no, users_laptop)