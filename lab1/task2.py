# Інвентаризація продуктів. Створіть словник, де ключі - це назви продуктів,
# а значення - їх кількість на складі. Напишіть функцію, яка приймає назву
# продукту та кількість, і оновлює словник відповідно до додавання або видалення продуктів.
# Додатково: створіть список продуктів, в яких кількість менше ніж 5.

inventory = {
    "apple": 3,
    "banana": 3,
    "orange": 4,
    "milk": 2,
    "bread": 5
}

def update_inventory(product, amount):
    if product in inventory:
        inventory[product] += amount
    else:
        inventory[product] = amount

while True:
    product_name = input("Enter the product name (or type 'stop' to finish): ").lower()
    if product_name == "stop":
        break
    amount = int(input("Enter the amount (use negative number to remove or reduce the amount): "))
    update_inventory(product_name, amount)

low_stock = [item for item, quantity in inventory.items() if quantity < 5]

print("Updated inventory:", inventory)
print("Products with less than 5 items:", low_stock)
