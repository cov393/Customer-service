active = True
is_admin = False

import uuid

'''Generating the unique id numbers'''
def id_generator():
    id = (uuid.uuid1())   
    # print(id)
    return str(id)


'''Calculating the total price'''
def calc_total_price(qty, pri):
    quantity = int(qty)
    price = int(pri)
    total_price = quantity * price

    return str(total_price)


'''Display the menu for users and admin'''
def menu():
    print('Please choose one of the following from menu:\n')
    print('1. Insert Customer Details')
    print("2. Insert Product")
    print("3. Display Products")
    # print("4. Orders Placed")
    print("99 Admin Access")
    print("0. Exit")

    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        inserting_customer_details()

    if user_input == 2:
        inserting_products()

        '''ADMIN!!!'''
    if user_input == 99:
        admin_menu()

    '''Quitting the session'''
    if user_input == 0:
        quit()

    if user_input == 3:
        display_products()

    # if user_input == 4:
    #     display_orders_placed()


'''Admin Menu'''

def admin_menu():
    authorized = False                                  # user is not authorized
    while not authorized:                               # starting the loop
        password = input("Please enter the admin PIN: ")

        if password == str(2468):                       # password have to be 2468
            authorized = True                           # after admin can login
        else:
            print("Incorrect Pin \n")


    '''Displaying an admin menu'''

    print("1: Total sales from Product ID")  
    print("2: Total sales from category") 
    print("3: Total sales from price range")
    print("4: Total sales from location")          
    print("5: Back to main menu")
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        total_sales_from_product_id()                   # starting function - total_sales_from_product_id()
    if user_input==2:
        total_sales_from_category()
    if user_input==3:
        total_sales_from_price_range()
    if user_input == 4:
        total_sales_from_location()         
    if user_input == 5:                                 # starting function - menu()
        menu()


#--------------DATABASE LIST------------


categories = [["CatId",  id_generator(), id_generator(), id_generator()], ["CatName", "Televisions", "Hair Care", "DIY"],
              ["CatDescription"]]

products = [["Pid", id_generator(), id_generator(), id_generator()],
            ["PName", "Samsung Television", "Head & Shoulders Shampoo", "DeWalt Power Drill"],
            ["Price", "299", "6", "85"],
            ["CategoryId", categories[0][1], categories[0][2], categories[0][3]]]

customers = [["CustomerId", id_generator(), id_generator(), id_generator()],
             ["Email", "joebloggs@outlook.com", "billybob@gmail.co.uk", "jane@outlook.com"],
             ["PhoneNumber", "07294837284", "07283029382", "07228374632"],
             ["Address", "Braichyrhenllysg Cottages", "Bryncrug,LL36 9PR", "Mulberry, London Road, Coldwaltham,RH20 1LR",
              "Trem Moelwyn, Croesor,LL48 6SR"], ["Location", "London", "Sheffield", "Manchester"],
             ["Country", "United Kingdom", "United Kingdom", "United Kingdom"]]

orders_placed = [["OrderId", id_generator(), id_generator(), id_generator()],
                 ["Pid", products[0][1], products[0][2], products[0][3]], ["Quantity", "2", "4", "3"],
                 ["TotalPrice", str(2 * products[2][0]), str(4 * products[2][1]), str(3 * products[2][2])],
                 ["CustomerId", customers[0][1], customers[0][1], customers[0][2]],
                 ["Status", "Shipping", "Shipping", "Delivered"]]

# def orders_places():
#     user_email=input("To see your order details, please type your email:")


#---------FUNCTION FOR USER, SO THEY CAN INSERT NEW ITEMS IN CART---------
'''CatID | CatName | CarDescription'''

def inserting_category():
    '''CatID'''
    cat_ID=[]
    cat_name=[]
    cat_description=[]
    new_cat_ID=(uuid.uuid1())                           # unique category ID generation
    cat_ID.append(new_cat_ID)                           # inserting "new category ID" to DB

    '''CatName'''
    new_cat_name=input('Category Name: ')
    cat_name.append(new_cat_name)
    
    '''CatDescription'''
    new_cat_description=input('Category Description: ')
    cat_description.append(new_cat_description)


def total_sales_from_category():
    category_id = input("Enter the category id you want to view total sales for: ")
    total_sales = 0

    while not valid_category_id():
        category_id = input("Enter the category id you want to view total sales for: ")

    # for i in range()


def total_sales_from_product_id():
    print(products)
    product_id = input("Enter the product id you want to view total sales for:  ")
    total_sales = 0

    while not valid_product_id(product_id):
        product_id = input("Enter the product id you want to view total sales for:  ")

    for i in range(0, len(orders_placed[1])):
        if product_id == orders_placed[1][i]:
            total_sales = + int(orders_placed[2][i])

    print("total sales for product id {} is {}".format(product_id, total_sales))

def total_sales_from_category():
    category_name = input("Enter the category name you want to view total sales for: ")
    total_sales = 0
    category_id = ""
    products_in_category = []

    while not valid_category_name(category_name):
        category_name = input("Enter the category id you want to view total sales for: ")

    # get the category id
    for i in range(0, len(categories[1])):
        if category_name == categories[1][i]:
            category_id = categories[0][i]

    # get all products in a category
    for i in range(0, len(products[1])):
        if category_id == products[3][i]:
            products_in_category.append(products[0][i])

    # for i in range(0, len(products_in_category)):

    # for i in range(0, len(orders_placed[0])):
    #     for j in range(0, len(products_in_category[0])):
    #         pass
    #     if orders_placed[1][i] == products_in_category[i]:
    #         total_sales += orders_placed[2][i]

    for i in range(0, len(orders_placed[0])):
        for j in range(0, len(products_in_category)):
            if orders_placed[1][i] == products_in_category[j]:
                total_sales += int(orders_placed[2][i])

    print("{} products have a total sales of {}".format(category_name, total_sales))

    # for i in range(0, len(products[0])):
    #     if product_id == products[0][i]:
    #         for j in range(0, len(orders_placed[0])):
    #             if orders_placed[1][j] == product_id:
    #                 total_price = + int(orders_placed[2][j])
    #     else:
    #         print("This product id does not exist")
    # print("Total sales from product id {} is £{}".format(product_id, total_price))

def total_sales_from_location():
    print(customers[4])
    product_location=input("Enter the product location: ")
    total_sales=0

    while not valid_customer_location(product_location):
        product_price=input("Enter the product location: ")
    
    for i in range(0,len(customers[4])):
        if product_location ==customers[3][i]:
            # print(customers[3][i])
            total_sales= + int(customers[3][i])
            print(customers[3][i])
    print('total sales from location {} is {}'.format(product_location,total_sales))


def valid_customer_location(input):
    valid = False

    for i in range(0, len(customers[4])):
        if input == customers[4][i]:
            valid = True

    if not valid:
        print("Location does not exist, please enter a valid location \n")

    return valid  


def total_sales_from_price_range():
    print(products)
    product_price=input("Enter the product price: ")
    total_sales=0

    while not  valid_category_price(product_price):
        product_price=input("Enter the product price: ")
    
    for i in range(0,len(products[2])):
        if product_price ==products[2][i]:
            total_sales= + int(products[2][i])
            print(products[3][i])
    print('total sales from price range is {}'.format(product_price,total_sales))

def valid_customer_id(input):
    valid = False

    for i in range(0, len(customers[0])):
        if input == customers[0][i]:
            valid = True

    if not valid:
        print("Customer Id does not exist, please enter a valid customer id \n")

    return valid


def valid_category_id(input):
    valid = False

    for i in range(0, len(categories[0])):
        if input == categories[0][i]:
            valid = True

    if not valid:
        print("Category Id does not exist, please enter a valid category id \n")

    return valid


def valid_product_id(input):
    valid = False

    for i in range(0, len(products[0])):             # checking the first item in the product list
        # print(len(products[0]))
        if input == products[0][i]:
            # print(len(products[0][i]))
            valid = True

    if not valid:
        print("Product Id does not exist, please enter a valid product id")

    return valid


def valid_category_name(input):
    valid = False

    for i in range(0, len(categories[1])):
        if input == categories[1][i]:
            valid = True

    if not valid:
        print("Category Id does not exist, please enter a valid category id \n")

    return valid

def valid_category_price(input):
    valid = False

    for i in range(0, len(products[2])):
        if input == products[2][i]:
            valid = True

    if not valid:
        print("Category Id does not exist, please enter a valid category id \n")

    return valid

def inserting_products():
    # pid calculated automatically
    product_id = id_generator()
    product_name = input("Insert Product Name: ")
    product_price = input("Insert Product Price: ")
    category_id = input("Enter a valid category Id: ")
    while (valid_category_id(category_id) != True):
        category_id = input("Enter a valid category Id: ")
    products[0].append(product_id)
    products[1].append(product_name)
    products[2].append(product_price)
    products[3].append(category_id)


def inserting_customer_details():
    cust_ID = []
    cust_email = []
    cust_phone_number = []
    '''YES/NO/Return'''
    status_received = []
    address = []
    location = []
    country = []
    new_cust_ID = (uuid.uuid1())
    cust_ID.append(new_cust_ID)
    new_cust_email = input('Email address (.com), (.org), (.co), (.in): ')
    while new_cust_email not in cust_email:
        if new_cust_email.endswith('.com') or new_cust_email.endswith('.org') or new_cust_email.endswith(
                '.co') or new_cust_email.endswith('.in'):
            cust_email.append(new_cust_email)
            cust_email.append(new_cust_email)
        else:
            return False
        
    print('Your phone number must start from (+) or (0) and contain 11 characters ')
    new_cust_phone_number = input("Enter you phone number: ")
    while new_cust_phone_number not in cust_phone_number:
        if new_cust_phone_number.startswith('+') or new_cust_phone_number.startswith('0'):
            cust_phone_number.append(new_cust_phone_number)
        else:
            print('please, try again.\n')
            return False
    print('Order status: (y)- Yes, (n) - No, (r)- Return')
    new_status_received = input('Order Status: ')
    while new_status_received not in status_received:
        if new_status_received == 'y':
            new_status_received = 'Yes'
            status_received.append(new_status_received)
        elif new_status_received == 'n':
            new_status_received = 'No'
            status_received.append(new_status_received)
        elif new_status_received == 'r':
            new_status_received = 'Return'
            status_received.append(new_status_received)
        else:
            return False
    new_address = []
    street = input('Street: ')
    house_number = input('House number: ')
    while new_address not in address:
        # street=input('Street: ')
        # house_number=input('House number: ')
        if house_number.isdigit:
            postcode = input('Postcode: ')
            new_address.append(street)
            new_address.append(house_number)
            new_address.append(postcode)
            address.append(new_address)
        else:
            print('please try again ')
            return False
    new_location = input(" Enter your location: ")
    while new_location not in location:
        location.append(new_location)
    new_country = input('Country: ')
    while new_country not in country:
        country.append(new_country)
    # print(cust_ID)
    # print(cust_email)
    # print(cust_phone_number)
    # '''YES/NO/Return'''
    # print(status_received)
    # print(address)
    # print(location)
    # print(country)


# def orders_placed():
#     for i in range(0, len(orders_placed)):
#         # print("Order Id: {}, Product Id: {}, Quantity: {}, Total Price: {}, Customer Id: {}, Status {}").format(
#         #     orders_placed[0][i], orders_placed[1][i], orders_placed[2][i], orders_placed[3][i], orders_placed[4][i],
#         #     orders_placed[5][i])
#         print("test")

def display_orders_placed():
    customer_id = input("Enter your customer id to view your orders: ")

    while not valid_customer_id(customer_id):
        customer_id = input("Enter your customer id to view your orders: ")

    for i in range(0, len(orders_placed[0])):
        if orders_placed[3][i] == customer_id:
            print("")


def shipped_orders():
    pass


def display_products():
    for i in range(1, len(products[0])):
        print(
            "Pid: {}, Product Name: {}, Price: {}, CategoryId: {}".format(products[0][i], products[1][i],
                                                                          products[2][i], products[3][i]))


while (active):
    menu()
