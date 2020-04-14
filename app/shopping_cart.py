# shopping_cart.py

from dotenv import load_dotenv
import os

load_dotenv()

# MODULES
from datetime import datetime

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

def human_friendly_timestamp(now):
    """
    Converts datetime information into a human friendly string
    Param: now
    Example:
        current_year = 2020
        current_month = 4
        current_day = 13
        current_hour = 17
        current_minute = 25
        current_second = 12
    Returns: 2020-4-13 5:25pm
    """
    return datetime.now().strftime("%m/%d/%Y %I:%M %p")

def dashed_line():
    """
    Prints a dashed line to improve receipt readability
    Param: none
    Example: dashed_line()
    Returns: "---------------------"
    """
    print("--------------------")

def find_product(product, list):
    """
    Returns the correct product in a list that matches a given identifier number
    Param: product identifier (integer)
    Example: find_product(1)
    Returns: product[0]["name"]
    """
    matching_products = [p for p in products if str(p["id"]) == str(scanned_id)]
    matching_product = matching_products[0]
    return matching_product

def calculate_tax(tax_rate, subtotal_price):
    """
    This will calcuate the tax using the subtotal amount
    Param: subtotal_price (any int or float amt)
    Example: calculate_tax(15.00)
    Returns: (15.00 * tax rate)
    """
    tax_amt = tax_rate * subtotal_price
    return float(tax_amt)

def calculate_total_price():
    """
    Calculates the total price for a list of products
    Param: list of products
    Example: [4.00, 5.00, 2.00, 10.50]
    Returns: (4+5+2+10.50)*(1+ tax rate) = 23.38
    """
    total_price = float(subtotal_price * (1 + tax_rate))
    return total_price

if __name__ == "__main__":

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

    #DEFINED VARIABLES
    subtotal_price = 0
    total_price = 0
    scanned_ids = [] #this will be a list to store scanned_id's and print after all id's have been entered
    now = datetime.now()
    tax_rate = float(os.environ.get("TAX_RATE"))

    #LOOP 
    while True:
        scanned_id = input("Please enter a product ID number, or DONE: ")
        if scanned_id.upper() == "DONE":
            break
        elif int(scanned_id) > 20 or int(scanned_id) < 1:
            print("This ID is not registered. Please enter a different ID or DONE.") 
        else:
            scanned_ids.append(scanned_id)

    #
    #Printing Receipt
    #
    dashed_line()
    print("Gregarious Groceries")
    print("915 7th Ave, New York City, NY 10019")
    dashed_line()
    print("Purchased: " + human_friendly_timestamp(now))
    dashed_line()
    print("Today you purchased: ")
    for scanned_id in scanned_ids:
            matching_product = find_product(scanned_id, products)
            print(" * " + str(matching_product["name"]) + " " + to_usd(matching_product["price"]))   
            subtotal_price = subtotal_price + matching_product["price"]  
    dashed_line()
    print(f"Subtotal: {to_usd(subtotal_price)}")
    print(f"Tax: {to_usd(calculate_tax(tax_rate,subtotal_price))}")
    print(f"Total amount: {to_usd(calculate_total_price())}")
    dashed_line()
    print("Have a GREGARIOUS day and we hope to see you again soon!")
    print("Check us out at www.gregariousgroceries.com or give us a call at 202-954-3232")
    dashed_line()
