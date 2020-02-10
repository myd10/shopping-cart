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

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output



#
# Input information / ID
#

#defined variables
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


#loop
while True:
    scanned_id = input("Please enter a product ID number: ") #input returns a string datatype
    if scanned_id == "DONE":
        break
    else:
        scanned_ids.append(scanned_id)

for scanned_id in scanned_ids:
        matching_products = [p for p in products if str(p["id"]) == str(scanned_id)]
        matching_product = matching_products[0] #I have gotten an error here that the index is out of range
        subtotal_price = subtotal_price + matching_product["price"]
        print(str(matching_product["name"]) + " " + str(matching_product["price"]))
        
#print(matching_products)

#print(type(scanned_id))
#print(scanned_id)


#
# Calculate, filter out bad answers, and display
#

#tax amount
tax_amt = .10 * float(subtotal_price)

#total 
total_price = subtotal_price + tax_amt

#
# Displaying results
#

#HEADING
print("---------------")
print("Gregarious Groceries")
print("---------------")

#time of purchase
print("Purchased at " + str(current_time) + " on " + str(current_month) + "/" + str(current_day) + "/" + str(current_year))

#What was purchased
print("---------------")
print("Today you purchased: ")

#Total cost
print("---------------")
print("Subtotal: $" + f"${subtotal_price:,.2f}")
print("Tax: $" + f"${tax_amt:,.2f}")
print("Total amount: " + f"${total_price:,.2f}")

#Thank you and come back
print("---------------")
print("For questions, comments, and concerns visit www.gregariousgroceries.com or give us a call at 202-954-3232")
print("Have a GREGORIOUS day and we hope to see you again soon!")
#print("\U0001f600")



# A grocery store name of your choice
# A grocery store phone number and/or website URL and/or address of choice
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
# The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
# The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
# A friendly message thanking the customer and/or encouraging the customer to shop again
# shopping_cart.py
