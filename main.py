# Ask for the customer's name
customer_name = input("Enter the customer's name: ")

# Initialize the variable to store the total value of the purchase
total_value = 0

# Ask for the quantity and price of each product
product1_quantity = int(input("Enter the quantity of product 1: "))
product1_price = float(input("Enter the unit price of product 1: "))

product2_quantity = int(input("Enter the quantity of product 2: "))
product2_price = float(input("Enter the unit price of product 2: "))

# Calculate the total value of the purchase
total_value = (product1_quantity * product1_price) + (product2_quantity * product2_price)

# Display the receipt to the customer
print("------- RECEIPT -------")
print("Customer: ", customer_name)
print("Product 1 - Quantity:", product1_quantity, " Unit Price:", product1_price)
print("Product 2 - Quantity:", product2_quantity, " Unit Price:", product2_price)
print("Total value of the purchase: $", total_value)