def get_customer():
    print("=== Customer Information ===")
    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")
    quantity = int(input("Quantity : "))
    price = float(input("Price per Item (RM): "))
    delivery = input("Delivery (Y/N): ")
    
    delivery_charges = 0.0
    if delivery.upper() == 'Y':
        delivery_charges = 5.00
        
    return name, food, quantity, price, delivery_charges