from customer import get_customer
from receipt import print_receipt

def main():
    # Getting the customer data
    name, food, quantity, price, delivery_charges = get_customer()
    
    # Printing out the food receipt
    print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()