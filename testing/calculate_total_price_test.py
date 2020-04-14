#calculate_total_price.py
#testing the calculate_total_price function

from app.shopping_cart import calculate_total_price

def test_calculate_total_price():
    result = calculate_total_price(10, .1)
    assert result == 11

#passed