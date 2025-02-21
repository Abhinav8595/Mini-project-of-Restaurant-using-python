# Menu 
menu = {
    'Pizza': 50,
    'Pasta': 60,
    'Burger': 50,
    'coffee': 80,
    'Salad': 50,
}

# Greet
print("Welcome to Rishu Restaurant")
print(" Pizza: Rs.50\n Pasta: Rs.60\n Burger: Rs.50\n coffee: Rs.80\n Salad: Rs.50")

order_total = 0

# First Order
item_1 = input("Enter the name of your item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

# Second Order (Optional)
another_order = input("Do you want to add another item? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"'{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")

# ✅ Total amount is shown regardless of what happens above
print(f"The total amount of items to pay is Rs.{order_total}")
