from food_order import calculate_total as food_order

def test_order1():
    assert food_order(10, 2) == 20

# test if total food order is equal to 30
def test_order_30():
    assert food_order(15, 2) == 30

# test if total food order is equal to 100
def test_order_100():
    assert food_order(20, 5) == 100

# test if total food order is equal to 10
def test_order_10():
    assert food_order(5, 2) == 10

# test if total food order is equal to "invalid price"
def test_invalid_price():
    assert food_order(-5, 2) == "invalid price"

# test if total food order is equal to "invalid quantity"
def test_invalid_quantity():
    assert food_order(10, 0) == "invalid quantity"
    assert food_order(10, -3) == "invalid quantity"