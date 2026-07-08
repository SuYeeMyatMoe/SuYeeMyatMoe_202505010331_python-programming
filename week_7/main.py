from food_order import calculate_total

def main():
    price = float(input("Price (RM): "))
    quantity = int(input("Quantity: "))

    total = calculate_total(price, quantity)

    # Bug fix: Check if the return value is a string (error message) before formatting
    if isinstance(total, str):
        print(f"Order Failed: {total}")
    else:
        print(f"Total Payment = RM {total:.2f}")

if __name__ == "__main__":
    main()