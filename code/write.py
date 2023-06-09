""" Importing the required function from read.py and datetime object of datetime modue """
from read import read_laptop_list
from datetime import datetime


def update_stock(laptop_id, quantity, kind):
    """This function updates the stock of laptop depending on the nature of transaction"""
    laptops = read_laptop_list()

    amt = laptops[laptop_id][3]
    if kind == 'sales':
        # decrease the stock
        (laptops[laptop_id])[3] = ' ' + str(int(amt[1:]) - quantity)

    else:
        # increase the stock
        (laptops[laptop_id])[3] = ' ' + str(int(amt[1:]) + quantity)

    file = open('Laptops.txt', 'w')
    # Write the updated values into text file
    for laptop in laptops.values():
        file.write(f"{laptop[0]},{laptop[1]},{laptop[2]},{laptop[3]},{laptop[4]},{laptop[5]},{laptop[6]},{laptop[7]}\n")

    file.close()


def generate_purchase_invoice(name, address, phone, users_laptop):
    """This function generates the invoice for laptop purchase in terminal and in text file"""
    dt = datetime.now()
    dt_string = dt.strftime("%d/%m/%Y %H:%M")
    # storing date and time
    date_now = dt_string.split(' ')[0]
    time_now = dt_string.split(' ')[1]
    inv = open(f'{name}.txt', 'w')
    print("\nInvoice\n")
    print(f"Name : {name}")
    inv.write(f"Name : {name}\n")
    print(f"Address : {address}")
    inv.write(f"Address : {address}\n")
    print(f"Phone no : {phone}")
    inv.write(f"Phone no : {phone}\n")
    print(f"Date : {date_now}")
    inv.write(f"Date : {date_now}\n")
    print(f"Time : {time_now}")
    inv.write(f"Time : {time_now}\n")
    print("\n")
    inv.write("\n")
    index = 1
    total_amount = 0
    for items in users_laptop:
        print(f"Item {index}")
        inv.write(f"Item {index}\n")
        print(f"Laptop ID : {items[0]}")
        inv.write(f"Laptop ID : {items[0]}\n")
        print(f"Laptop Name : {items[1]}")
        inv.write(f"Laptop Name : {items[1]}\n")
        print(f"Laptop Brand : {items[2]}")
        inv.write(f"Laptop Brand : {items[2]}\n")
        print(f"Laptop Quantity : {items[3]}")
        inv.write(f"Laptop Quantity : {items[3]}\n")
        qty = items[3]
        print(f"Price : {items[4]}")
        inv.write(f"Price : {items[4]}\n")
        total_amount += (int(items[4].replace(' $', '')) * qty)
        inv.write("\n")
        print("\n")
        index += 1
    print(f"Total amount (Without VAT) : ${total_amount}")
    inv.write(f"Total amount (Without VAT) : ${total_amount}\n")
    print(f"VAT amount : ${0.13 * total_amount}")
    inv.write(f"VAT amount : ${0.13 * total_amount}\n")
    print(f"Total amount (With VAT) : ${total_amount + 0.13 * total_amount}")
    inv.write(f"Total amount (With VAT) : ${total_amount + 0.13 * total_amount}\n")
    inv.close()


def generate_sales_invoice(name, address, phone, users_laptop, shipment):
    """This function generates the invoice for laptop sales in terminal and in text file"""
    dt = datetime.now()
    dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")
    # storing date and time
    date_now = dt_string.split(' ')[0]
    time_now = dt_string.split(' ')[1]
    inv = open(f'{name}.txt', 'w')
    print("\nInvoice\n")
    print(f"Name : {name}")
    inv.write(f"Name : {name}\n")
    print(f"Address : {address}")
    inv.write(f"Address : {address}\n")
    print(f"Phone no : {phone}")
    inv.write(f"Phone no : {phone}\n")
    print(f"Date : {date_now}")
    inv.write(f"Date : {date_now}\n")
    print(f"Time : {time_now}")
    inv.write(f"Time : {time_now}\n")
    print("\n")
    inv.write("\n")
    index = 1
    total_amount = 0
    for items in users_laptop:
        print(f"Item {index}")
        inv.write(f"Item {index}\n")
        print(f"Laptop ID : {items[0]}")
        inv.write(f"Laptop ID : {items[0]}\n")
        print(f"Laptop Name : {items[1]}")
        inv.write(f"Laptop Name : {items[1]}\n")
        print(f"Laptop Brand : {items[2]}")
        inv.write(f"Laptop Brand : {items[2]}\n")
        print(f"Laptop Quantity : {items[3]}")
        inv.write(f"Laptop Quantity : {items[3]}\n")
        qty = items[3]
        print(f"Price : {items[4]}")
        inv.write(f"Price : {items[4]}\n")
        total_amount += (int(items[4].replace(' $', '')) * qty)
        inv.write("\n")
        print("\n")
        index += 1

    if shipment:
        print(f"Total amount (excluding shipping cost) : ${total_amount}")
        inv.write(f"\nTotal amount (excluding shipping cost) : ${total_amount}\n")
        print(f"Shipping cost : $5")
        inv.write(f"Shipping cost : $5\n")
        print(f"Total amount (including shipping cost) : ${total_amount + 5}")
        inv.write(f"Total amount (including shipping cost) : ${total_amount + 5}\n")

    else:
        print(f"Total amount : ${total_amount}")
        inv.write(f"\nTotal amount : ${total_amount}\n")
    inv.close()


def display_laptops():
    """This function displays all the information of available laptops in tabular format"""
    print("<-----------------------------------------------------------Information of Laptops in our Shop----------------------------------------------------------------->\n\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ID         Laptop Name                 Brand        Price    Quantity       CPU                       GPU                RAM            Storage")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sn = 1
    laptops = read_laptop_list()  # store the dictionary returned by read_laptop_list function
    for lpt in laptops.values():
        print(f" {sn}\t\t\t{lpt[0]}\t\t{lpt[1]}\t\t{lpt[2]}\t\t{lpt[3]}\t\t{lpt[4]}\t\t{lpt[5]}\t\t{lpt[6]}\t\t{lpt[7]}")
        sn += 1
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")