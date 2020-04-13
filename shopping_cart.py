# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


#GOAL 1: fix USD formatting
#GOAL 2: fix date and time function, display friendly human message without so much code
#GOAL 3: write data to CSV?
#Goal 4: get rid of reptition
#GOAL 5: testing
#GOAL 6: hit all checkpoints on product outline. 


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#
# Input information / ID
#

#DEFINED VARIABLES
subtotal_price = 0
tax_amt = 0
total_price = 0
scanned_ids = [] #this will be a list to store scanned_id's and print after all id's have been entered
grocery_list = []

#date and time, help from https://www.youtube.com/watch?v=WB5eMfnBI-8
from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H:%M:%S") #help from https://www.programiz.com/python-programming/datetime/current-time
current_year = now.year
current_month = now.month
current_day = now.day
current_hour = now.hour
current_minute = now.minute

#loop and control over ids accepted
while True:
    scanned_id = input("Please enter a product ID number, or DONE: ") #input returns a string datatype
    if scanned_id == "DONE":
        break
    elif int(scanned_id) > 20 or int(scanned_id) < 1:
        print("This ID is not registered. Please enter a different ID.") 
    else:
        scanned_ids.append(scanned_id)

#HEADING
print("---------------")
print("Gregarious Groceries")
print("915 7th Ave, New York City, NY 10019")
print("---------------")

#TIME AND DATE
if int(current_hour) > 12 and int(current_minute) > 9:
    print("Purchased at " + str(current_hour - 12) + ":" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
elif int(current_hour) > 12 and int(current_minute) < 9:
    print("Purchased at " + str(current_hour - 12) + ":0" + str(current_minute) + "pm on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
elif int(current_hour) < 12 and int(current_minute) < 9:
    print("Purchased at " + str(current_hour) + ":0" + str(current_minute) + "am on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))
else:
    print("Purchased at " + str(current_time) + "am on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))

#PURCHASED ITEMS
print("---------------")
print("Today you purchased: ")

for scanned_id in scanned_ids:
        matching_products = [p for p in products if str(p["id"]) == str(scanned_id)]
        matching_product = matching_products[0] #I have gotten an error here that the index is out of range
        subtotal_price = subtotal_price + matching_product["price"]
        print(" * " + str(matching_product["name"]) + " " + to_usd(matching_product["price"]))
    
#TOTAL COST
tax_amt = .0875 * float(subtotal_price)
total_price = subtotal_price + tax_amt

print("---------------")
print(f"Subtotal: {to_usd(subtotal_price)}")
print(f"Tax: {to_usd(tax_amt)}")
print(f"Total amount: {to_usd(total_price)}")

#Thank you and come back
print("---------------")
print("Have a GREGARIOUS day and we hope to see you again soon!")
print("Check us out at www.gregariousgroceries.com or give us a call at 202-954-3232")
print("---------------")


#Basic Requirements
# A grocery store name of your choice 
# A grocery store phone number and/or website URL and/or address of choice 
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
# The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
# The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
# A friendly message thanking the customer and/or encouraging the customer to shop again

# shopping_cart.py

#possible email attachment for future
#er = input("Would you like an email copy of your recipet [y/n] ").lower()
#
#if er == "y":
#    input("Please enter your email address: ")
#else:
#    print("Okay! Have a great day!")
#    quit()