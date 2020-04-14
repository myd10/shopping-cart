# testing the to_usd function
# I think I can test everything in here
# I am not sure yet

from app.shopping_cart import to_usd

def test_to_usd():
    result = to_usd(4000.4444)
    assert result == "$4000.44"


