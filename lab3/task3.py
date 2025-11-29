import json
import matplotlib.pyplot as plt

with open("task1.json", "r", encoding="utf-8") as file:
    data = json.load(file)

dates = [item["exchangedate"] for item in data]
rates = [item["rate"] for item in data]

plt.figure(figsize=(10, 5))
plt.plot(dates, rates, marker='o')

plt.title("Exchange rate (from Postman data)")
plt.xlabel("Date")
plt.ylabel("Rate (UAH)")
plt.grid(True)
plt.tight_layout()
plt.savefig("currency_plot.png")
plt.show()
