def calculate_total(price, quantity):
    # Validate customer input to prevent invalid orders
    if price < 0:
        return "invalid price"
    if quantity <= 0:
        return "invalid quantity"
    
    # Calculate and return total
    return price * quantity