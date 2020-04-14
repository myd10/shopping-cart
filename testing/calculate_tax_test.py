#calculate_tax_test.py
#testing the calculate_tax function

from app.shopping_cart import calculate_tax

def test_calculate_tax():
    result = calculate_tax(.0875, 10)
    assert result == 0.875

#passed