#human_friendly_timestamp_test.py
#testing the human_friendly_timestamp function


from app.shopping_cart import human_friendly_timestamp
from datetime import datetime

def test_human_friendly_timestamp():
    now = datetime(2020, 4, 14, 16, 25, 10)
    result = human_friendly_timestamp(now)
    assert result == "04/14/2020 04:25 PM"
