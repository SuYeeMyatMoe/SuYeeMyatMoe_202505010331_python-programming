def calculate_total(coffee, tea, sandwich):
    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00
    
    total = (coffee * coffee_price) + (tea * tea_price) + (sandwich * sandwich_price)
    return total

def print_receipt(customer_name, coffee, tea, sandwich):
    # Calculate the total inside the receipt function using the other utility function
    total = calculate_total(coffee, tea, sandwich)
    
    print("\n===== RECEIPT =====")
    print(f"Customer : {customer_name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-" * 19)
    print(f"Total = RM {total:.2f}")