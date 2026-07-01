# main.py
import utils

def main():
    # Gather inputs based on the sample format
    customer_name = input("Customer name: ")
    coffee_qty = int(input("Coffee quantity: "))
    tea_qty = int(input("Tea quantity: "))
    sandwich_qty = int(input("Sandwich quantity: "))
    
    # Call the print_receipt function from utils.py
    utils.print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty)

if __name__ == "__main__":
    main()