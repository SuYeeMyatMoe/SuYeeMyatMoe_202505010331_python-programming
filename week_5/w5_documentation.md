# Week 5 - Tutorial 5 Documentation

## 1.1 Problem Statement
The cafe currently calculates customer bills manually, which can be inefficient and prone to error. The goal is to build an automated Python program that takes the customer's order quantities and automatically calculates the total bill based on a fixed pricing menu.

## 1.2 Inputs
* Customer Name (String)
* Quantity of Coffee (Integer)
* Quantity of Tea (Integer)
* Quantity of Sandwiches (Integer)

## 1.3 Outputs
* A formatted receipt displaying:
    * Customer name
    * Quantities of each item ordered
    * The total calculated bill in RM (Ringgit Malaysia)

## 1.4 Typical Process Flow
1. **Input**: Prompt the user to enter the customer's name and the quantity of coffee, tea, and sandwiches ordered.
2. **Process**: Calculate the total price by multiplying the quantity of each item by its fixed price (Coffee: RM 8.50, Tea: RM 6.00, Sandwich: RM 12.00) and summing the results.
3. **Output**: Generate and display a formatted receipt showing the inputted details and the final calculated total.

## 1.5 Constraints
* Item quantities must be whole, non-negative numbers (integers ≥ 0).
* The item prices are fixed and cannot be changed by the user (Coffee = 8.50, Tea = 6.00, Sandwich = 12.00).

## 2. Problem Decomposition

To solve this problem effectively, it can be broken down into three smaller, manageable tasks:

* **Task 1: Input Handling**
  Gather the necessary information from the user. This involves prompting the user for the customer's name (as a string) and the quantities of coffee, tea, and sandwiches ordered (as integers).

* **Task 2: Calculation Logic**
  Process the input data to determine the total bill. This involves creating a function that multiplies the quantity of each item by its respective fixed price (Coffee: RM 8.50, Tea: RM 6.00, Sandwich: RM 12.00) and adds them together to calculate the final total.

* **Task 3: Output Generation**
  Format and display the final results to the user. This involves creating a function that takes the customer details and the calculated total, and prints them out as a cleanly formatted receipt.

## 3. Pseudocode

```text
START
  // 1. Gather Inputs
  PROMPT user for customer_name
  PROMPT user for coffee_quantity
  PROMPT user for tea_quantity
  PROMPT user for sandwich_quantity
  
  // 2. Define Fixed Prices
  SET price_coffee = 8.50
  SET price_tea = 6.00
  SET price_sandwich = 12.00
  
  // 3. Calculate Total
  CALCULATE total_amount = (coffee_quantity * price_coffee) + 
                           (tea_quantity * price_tea) + 
                           (sandwich_quantity * price_sandwich)
  
  // 4. Print Output (Receipt)
  PRINT "===== RECEIPT ====="
  PRINT "Customer : " + customer_name
  PRINT "Coffee   : " + coffee_quantity
  PRINT "Tea      : " + tea_quantity
  PRINT "Sandwich : " + sandwich_quantity
  PRINT "-------------------"
  PRINT "Total = RM " + total_amount
END