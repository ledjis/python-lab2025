# Статистика продажів. Створіть список словників, де кожен словник
# представляє продаж з ключами: "продукт", "кількість", "ціна". Напишіть
# функцію, яка обчислює загальний дохід для кожного продукту та повертає словник,
# де ключі - це назви продуктів, а значення - загальний дохід. Створіть список продуктів,
# що принесли дохід більший ніж 1000.

sales = [
    {"product": "apple", "quantity": 400, "price": 10},
    {"product": "banana", "quantity": 120, "price": 5},
    {"product": "orange", "quantity": 80, "price": 8},
    {"product": "water", "quantity": 130, "price": 10},
    {"product": "milk", "quantity": 100, "price": 12}
]

def calculate_income(sales_list):
    income = {}
    for sale in sales_list:
        product = sale["product"]
        total = sale["quantity"] * sale["price"]
        if product in income:
            income[product] += total
        else:
            income[product] = total
    return income

total_income = calculate_income(sales)
high_income = [product for product, amount in total_income.items() if amount > 1000]

print("Total income by product:", total_income)
print("Products with income greater than 1000:", high_income)
