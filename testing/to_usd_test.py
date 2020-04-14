#to_usd_test.py
#testing the to_usd function

from app.shopping_cart import to_usd

def test_to_usd():
    result = to_usd(4000.4444)
    assert result == "$4,000.44"