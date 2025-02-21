# Mini-project-of-Restaurant-using-python
Mini project of Restaurant


1. Menu Definition
python
Copy
Edit
menu = {
    'Pizza': 50,
    'Pasta': 60,
    'Burger': 50,
    'coffee': 80,
    'Salad': 50,
}
A dictionary named menu is created with items as keys (e.g., 'Pizza', 'Pasta') and their corresponding prices as values (e.g., 50, 60).
This makes it easy to look up the price of an item using its name.


2. Greeting Message
python
Copy
Edit
print("Welcome to Rishu Restaurant")
print(" Pizza: Rs.50\n Pasta: Rs.60\n Burger: Rs.50\n coffee: Rs.80\n Salad: Rs.50")
print() displays messages to the user.
\n adds a newline after each item so that each menu item appears on a new line.


3. Initialize Order Total
python
Copy
Edit
order_total = 0
A variable order_total is initialized to 0 to keep track of the total bill as the user adds items.


4. First Order Input
python
Copy
Edit
item_1 = input("Enter the name of your item you want to order: ")
input() prompts the user to type in the name of the item they want to order.
The input is stored in the variable item_1.


5. First Order Validation
python
Copy
Edit
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")
Checks if the entered item exists in the menu dictionary.
If yes: Adds the price of the item to order_total and confirms the order.
If no: Prints an error message that the item is not available.


6. Second Order Option
python
Copy
Edit
another_order = input("Do you want to add another item? (yes/no): ").lower()
Asks the user if they want to add another item.
.lower() converts the input to lowercase to avoid issues with case sensitivity (e.g., "Yes" becomes "yes").


7. Second Order Validation
python
Copy
Edit
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"'{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")
If the user replies "yes":
Prompts for another item.
Checks if the new item is available in the menu.
Adds the price to order_total if available.
Otherwise, shows an error message.


8. Display Total Bill
python
Copy
Edit
print(f"The total amount of items to pay is Rs.{order_total}")
This line runs regardless of whether the user ordered one item or two.
Displays the total price of all the ordered items combined.
