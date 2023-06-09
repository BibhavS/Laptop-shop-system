def read_laptop_list():
    """This function reads the laptop details from txt file and returns dictionary of laptop details"""
    try:
        file = open('Laptops.txt', 'r')
        laptop_details = file.readlines()
        data = {}  # empty dictionary declaration
        laptop_id = 1
        for detail in laptop_details:
            item = detail.rstrip()
            lst = item.split(",")
            # update the data in dictionary
            data.update(
                {
                    laptop_id: lst
                }
            )
            laptop_id += 1

        file.close()
        # return dictionary of laptop details
        return data

    except FileNotFoundError:
        print("File is not found")






