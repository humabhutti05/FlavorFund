# print("hello")

# a = 8;
# b = 24;
# result=a/b
# print(result)
# Function to calculate salary
# def calculate_salary():
#     # Taking input from user for employee name
#     employee_name = input("Enter employee name: ")
    
#     # Taking input from user for employee salary
#     salary = float(input("Enter employee salary: "))
    
#     # Calculating tax based on salary
#     if salary > 50000:
#         tax = salary * 0.15
#     elif salary > 40000:
#         tax = salary * 0.1
#     elif salary <= 20000:  # Corrected condition here
#         tax = salary * 0.05
#     else:
#         tax = salary * 0.02
    
#     # Calculating net salary
#     net_salary = salary - tax
    
#     # Calculating P
#     p = salary * 0.1
    
#     # Printing net salary after deductions
#     print("Net salary for", employee_name, "is:", net_salary - p)

# # Calling the function to calculate salary
# calculate_salary()

# # Dictionary to store menu items and their prices
# menu = {
#     "burger": 5.99,
#     "pizza": 8.99,
#     "salad": 4.99,
#     "drink": 1.99
# }

# # Function to calculate the total cost of items ordered
# def calculate_total(order):
#     total_cost = 0
#     for item, quantity in order.items():
#         if item in menu:
#             total_cost += menu[item] * quantity
#     return total_cost

# # Function to apply discount based on total cost
# def apply_discount(total_cost, discount):
#     return total_cost * (1 - discount)

# # Function to display the menu
# def display_menu():
#     print("Menu:")
#     for item, price in menu.items():
#         print(item.capitalize() + ": $", price)

# # Function to take order input from the user
# def take_order():
#     order = {}
#     while True:
#         item = input("Enter item (or type 'done' to finish): ").lower()
#         if item == 'done':
#             break
#         if item in menu:
#             quantity = int(input("Enter quantity for {}: ".format(item)))
#             order[item] = quantity
#         else:
#             print("Sorry, {} is not in the menu.".format(item))
#     return order

# # Main function to run the program
# def main():
#     print("Welcome to Our Restaurant!")
#     display_menu()
#     order = take_order()
#     total_cost = calculate_total(order)
    
#     # Applying discount (10% discount for orders over $30)
#     discount = 0
#     if total_cost > 30:
#         discount = 0.1
    
#     discounted_cost = apply_discount(total_cost, discount)
    
#     print("\nOrder Summary:")
#     for item, quantity in order.items():
#         print(item.capitalize() + ": {} x ${}".format(quantity, menu[item]))
#     print("\nTotal cost before discount: $", total_cost)
#     print("Discount applied: {}%".format(discount * 100))
#     print("Total cost after discount: $", discounted_cost)
#     print("\nThank you for your order! Have a great day!")

# # Calling the main function to start the program
# if __name__ == "__main__":
#     main()

# Menu dictionary containing item names as keys and their respective prices as values
# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50
# }

# # Function to display the menu with prices
# def display_menu():
#     print("Menu:")
#     for item, price in menu.items():
#         print(f"{item}: Rs {price}")

# # Function to take orders from the user
# def take_order():
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#     return order

# # Function to calculate the total cost of the order
# def calculate_total(order):
#     total_cost = sum(menu[item] * quantity for item, quantity in order.items())
#     return total_cost

# # Function to apply discounts based on the total cost
# def apply_discount(total_cost):
#     if total_cost <= 3000:
#         discount_rate = 0.1
#     else:
#         discount_rate = 0.2
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# # Function to calculate tax
# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# # Function to generate and display the bill
# def generate_bill(order, total_cost, discounted_cost, tax_amount):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Final Amount (including tax): Rs {discounted_cost + tax_amount}")
#     print("*** Thank you for your order! ***")

# # Main function
# def main():
#     print("Welcome to our restaurant!")
#     display_menu()
#     order = take_order()
#     total_cost = calculate_total(order)
#     tax_amount = calculate_tax(total_cost)
#     discounted_cost = apply_discount(total_cost)
#     generate_bill(order, total_cost, discounted_cost, tax_amount)

# # Call the main function to start the program
# if __name__ == "__main__":
#     main()

# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50,
#     "Fries": 100,
#     "Pasta": 350,
#     "Sandwich": 200,
#     "Ice Cream": 120
# }

# generate_menu_card(menu)

# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")

#     discount_code = input("Do you have a discount code? (Enter code or type 'no'): ")
#     return order, discount_code

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50,
#     "Fries": 100,
#     "Pasta": 350,
#     "Sandwich": 200,
#     "Ice Cream": 120
# }

# generate_menu_card(menu)
# order, discount_code = take_order(menu)
# total_cost = sum(menu[item] * quantity for item, quantity in order.items())
# discounted_cost = apply_discount(total_cost, discount_code)
# tax_amount = calculate_tax(discounted_cost)
# delivery_charges = calculate_delivery_charges()
# generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)


# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#             generate_menu_card(menu)  # Display menu again
#     discount_code = input("Do you have a discount code? (Enter code or type 'no'): ")
#     return order, discount_code

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50,
#     "Fries": 100,
#     "Pasta": 350,
#     "Sandwich": 200,
#     "Ice Cream": 120
# }

# generate_menu_card(menu)
# order, discount_code = take_order(menu)
# total_cost = sum(menu[item] * quantity for item, quantity in order.items())
# discounted_cost = apply_discount(total_cost, discount_code)
# tax_amount = calculate_tax(discounted_cost)
# delivery_charges = calculate_delivery_charges()
# generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)

# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def create_user_account():
#     # This function can be expanded to include more details like name, email, etc.
#     user_name = input("Enter your name: ")
#     # Generate a discount code based on the user's name, for simplicity we'll use the first two characters
#     discount_code = user_name[:2].upper() + "10"  # Example: First two characters of name + "10"
#     return user_name, discount_code

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#     return order

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# # Create user account and discount code
# user_name, discount_code = create_user_account()
# print(f"Hello {user_name}! Your discount code is: {discount_code}")

# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50,
#     "Fries": 100,
#     "Pasta": 350,
#     "Sandwich": 200,
#     "Ice Cream": 120
# }

# generate_menu_card(menu)
# order = take_order(menu)
# total_cost = sum(menu[item] * quantity for item, quantity in order.items())
# discounted_cost = apply_discount(total_cost, discount_code)
# tax_amount = calculate_tax(discounted_cost)
# delivery_charges = calculate_delivery_charges()
# generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)

# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def create_user_account():
#     # This function can be expanded to include more details like name, email, etc.
#     user_name = input("Enter your name: ")
#     # Generate a discount code based on the user's name, for simplicity we'll use the first two characters
#     discount_code = user_name[:2].upper() + "10"  # Example: First two characters of name + "10"
#     return user_name, discount_code

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#     return order

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# # Create user account
# user_name, discount_code = create_user_account()

# # Prompt for discount code
# entered_discount_code = input("Enter your discount code (or type 'no' if you don't have one): ")
# if entered_discount_code.lower() == "no":
#     discount_code = "no"
# else:
#     # Check if entered discount code matches the generated discount code
#     if entered_discount_code != discount_code:
#         print("Invalid discount code. You won't get any discount.")
#         discount_code = "no"

# print(f"Hello {user_name}! Your discount code is: {discount_code}")

# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50,
#     "Fries": 100,
#     "Pasta": 350,
#     "Sandwich": 200,
#     "Ice Cream": 120
# }

# generate_menu_card(menu)
# order = take_order(menu)
# total_cost = sum(menu[item] * quantity for item, quantity in order.items())
# discounted_cost = apply_discount(total_cost, discount_code)
# tax_amount = calculate_tax(discounted_cost)
# delivery_charges = calculate_delivery_charges()
# generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)

# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def create_user_account():
#     # This function can be expanded to include more details like name, email, etc.
#     user_name = input("Enter your name: ")
#     # Generate a discount code based on the user's name, for simplicity we'll use the first two characters
#     discount_code = user_name[:2].upper() + "10"  # Example: First two characters of name + "10"
#     return user_name, discount_code

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#     return order

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# # Create user account and discount code
# user_name, discount_code = create_user_account()
# print(f"Hello {user_name}! Your discount code is: {discount_code}")

# menu = {
#     "Burger": 250,
#     "Pizza": 400,
#     "Salad": 150,
#     "Drink": 50,
#     "Fries": 100,
#     "Pasta": 350,
#     "Sandwich": 200,
#     "Ice Cream": 120
# }

# generate_menu_card(menu)
# order = take_order(menu)
# discount_code_input = input("Do you have a discount code? (Enter code or type 'no'): ")
# total_cost = sum(menu[item] * quantity for item, quantity in order.items())
# discounted_cost = apply_discount(total_cost, discount_code_input)
# tax_amount = calculate_tax(discounted_cost)
# delivery_charges = calculate_delivery_charges()
# generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)

# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def create_user_account():
#     # This function can be expanded to include more details like name, email, etc.
#     user_name = input("Enter your name: ")
#     # Generate a discount code based on the user's name, for simplicity we'll use the first two characters
#     discount_code = user_name[:2].upper() + "10"  # Example: First two characters of name + "10"
#     print(f"Hello {user_name}! Here is your discount code: {discount_code}. Enjoy your discount!")
#     return discount_code

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#     return order

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# # Create user account and discount code
# discount_code = create_user_account()
# want_to_buy = input("Would you like to buy? (yes/no): ").lower()

# if want_to_buy == "yes":
#     menu = {
#         "Burger": 250,
#         "Pizza": 400,
#         "Salad": 150,
#         "Drink": 50,
#         "Fries": 100,
#         "Pasta": 350,
#         "Sandwich": 200,
#         "Ice Cream": 120
#     }
    
#     generate_menu_card(menu)
#     order = take_order(menu)
#     discount_code_input = input("Do you have a discount code? (Enter code or type 'no'): ")
#     total_cost = sum(menu[item] * quantity for item, quantity in order.items())
#     discounted_cost = apply_discount(total_cost, discount_code_input)
#     tax_amount = calculate_tax(discounted_cost)
#     delivery_charges = calculate_delivery_charges()
#     generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)
# elif want_to_buy == "no":
#     print("Thank you for visiting!")
# else:
#     print("Invalid input. Please enter 'yes' or 'no'.")
# def generate_menu_card(menu):
#     print("*" * 40)
#     print("            Menu Card            ")
#     print("*" * 40)
#     print("{:<20} {:<10}".format("Item", "Price (Rs)"))
#     print("-" * 40)
#     for item, price in menu.items():
#         print("{:<20} {:<10}".format(item, price))
#     print("*" * 40)

# def create_user_account():
#     user_name = input("Enter your name: ")
#     # Generate a discount code based on the user's name, for simplicity we'll use the first two characters
#     discount_code = user_name[:2].upper() + "10"  # Example: First two characters of name + "10"
#     print(f"Hello {user_name}! Here is your discount code: {discount_code}. Enjoy your discount!")
#     return discount_code

# def take_order(menu):
#     order = {}
#     while True:
#         item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
#         if item == 'Done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s do you want to buy? "))
#             order[item] = quantity
#         else:
#             print("Sorry, we don't have that item in our menu. Please choose from the available options.")
#     return order

# def apply_discount(total_cost, discount_code):
#     if discount_code.lower() == "no":
#         return total_cost
#     # Implement your discount logic here based on the discount code
#     # For simplicity, let's assume a fixed discount rate of 10% for any code
#     discount_rate = 0.1
#     discounted_cost = total_cost * (1 - discount_rate)
#     return discounted_cost

# def calculate_tax(total_cost):
#     tax_rate = 0.05  # 5% tax rate
#     tax_amount = total_cost * tax_rate
#     return tax_amount

# def calculate_delivery_charges():
#     # Implement your delivery charges logic here
#     # For simplicity, let's assume a fixed delivery charge of Rs 50
#     return 50

# def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
#     print("\n*** Your Bill ***")
#     for item, quantity in order.items():
#         print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
#     print(f"\nTotal Cost: Rs {total_cost}")
#     print(f"Discount Applied: Rs {total_cost - discounted_cost}")
#     print(f"Tax Amount (5%): Rs {tax_amount}")
#     print(f"Delivery Charges: Rs {delivery_charges}")
#     print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
#     print("*** Thank you for your order! ***")

# want_discount = input("Would you like a Ramdan discount offer? (yes/no): ").lower()

# if want_discount == "yes":
#     discount_code = create_user_account()
# else:
#     discount_code = "no"

# want_to_buy = input("Would you like to buy? (yes/no): ").lower()

# if want_to_buy == "yes":
#     menu = {
#         "Burger": 250,
#         "Pizza": 400,
#         "Salad": 150,
#         "Drink": 50,
#         "Fries": 100,
#         "Pasta": 350,
#         "Sandwich": 200,
#         "Ice Cream": 120
#     }
    
#     generate_menu_card(menu)
#     order = take_order(menu)
#     discount_code_input = input("Do you have a discount code? (Enter code or type 'no'): ")
#     total_cost = sum(menu[item] * quantity for item, quantity in order.items())
#     discounted_cost = apply_discount(total_cost, discount_code_input)
#     tax_amount = calculate_tax(discounted_cost)
#     delivery_charges = calculate_delivery_charges()
#     generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)
# elif want_to_buy == "no":
#     print("Thank you for visiting!")
# else:
#     print("Invalid input. Please enter 'yes' or 'no'.")

def generate_menu_card(menu):
    print("*" * 40)
    print("            Menu Card            ")
    print("*" * 40)
    print("{:<20} {:<10}".format("Item", "Price (Rs)"))
    print("-" * 40)
    for item, price in menu.items():
        print("{:<20} {:<10}".format(item, price))
    print("*" * 40)

def create_user_account():
    user_name = input("Enter your name: ")
    # Generate a discount code based on the user's name, for simplicity we'll use the first two characters
    discount_code = user_name[:2].upper() + "10"  # Example: First two characters of name + "10"
    print(f"Hello {user_name}! Here is your discount code: {discount_code}. Enjoy your discount!")
    return discount_code

def take_order(menu):
    order = {}
    while True:
        item = input("Enter the item you want to buy (or type 'done' to finish): ").capitalize()
        if item == 'Done':
            break
        if item in menu:
            quantity = int(input(f"How many {item}s do you want to buy? "))
            order[item] = quantity
        else:
            print("Sorry, we don't have that item in our menu. Please choose from the available options.")
    return order

def apply_discount(total_cost, discount_code):
    if discount_code.lower() == "no":
        return total_cost
    # Implement your discount logic here based on the discount code
    # For simplicity, let's assume a fixed discount rate of 10% for any code
    discount_rate = 0.1
    discounted_cost = total_cost * (1 - discount_rate)
    return discounted_cost

def calculate_tax(total_cost):
    tax_rate = 0.05  # 5% tax rate
    tax_amount = total_cost * tax_rate
    return tax_amount

def calculate_delivery_charges():
    # Implement your delivery charges logic here
    # For simplicity, let's assume a fixed delivery charge of Rs 50
    return 50

def generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges):
    print("\n*** Your Bill ***")
    for item, quantity in order.items():
        print(f"{quantity} {item}s: Rs {menu[item] * quantity}")
    print(f"\nTotal Cost: Rs {total_cost}")
    print(f"Discount Applied: Rs {total_cost - discounted_cost}")
    print(f"Tax Amount (5%): Rs {tax_amount}")
    print(f"Delivery Charges: Rs {delivery_charges}")
    print(f"Final Amount (including tax and delivery charges): Rs {discounted_cost + tax_amount + delivery_charges}")
    print("*** Thank you for your order! ***")

# Welcome the user
print("Welcome FlavorFunds!")

want_discount = input("Would you like a discount offer? (yes/no): ").lower()

if want_discount == "yes":
    discount_code = create_user_account()
else:
    discount_code = "no"

want_to_buy = input("Would you like to buy? (yes/no): ").lower()

if want_to_buy == "yes":
    menu = {
        "Burger": 250,
        "Pizza": 400,
        "Salad": 150,
        "Drink": 50,
        "Fries": 100,
        "Pasta": 350,
        "Sandwich": 200,
        "Ice Cream": 120
    }
    
    generate_menu_card(menu)
    order = take_order(menu)
    discount_code_input = input("Do you have a discount code? (Enter code or type 'no'): ")
    total_cost = sum(menu[item] * quantity for item, quantity in order.items())
    discounted_cost = apply_discount(total_cost, discount_code_input)
    tax_amount = calculate_tax(discounted_cost)
    delivery_charges = calculate_delivery_charges()
    generate_bill(order, total_cost, discounted_cost, tax_amount, delivery_charges)
elif want_to_buy == "no":
    print("Thank you for visiting!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
