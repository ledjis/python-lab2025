import requests
from datetime import datetime, timedelta

today = datetime.today()
one_week_ago = today - timedelta(days=7)

end_date = today.strftime("%Y%m%d")
start_date = one_week_ago.strftime("%Y%m%d")

print("Type a currency code to check (usd, eur, pln...).")
print("Type 'exit' to finish.\n")

while True:
    currency = input("Enter currency code: ").lower()

    if currency == "exit":
        print("Program finished.")
        break

    url = (
        "https://bank.gov.ua/NBU_Exchange/exchange_site"
        f"?start={start_date}"
        f"&end={end_date}"
        f"&valcode={currency}"
        "&sort=exchangedate"
        "&order=desc"
        "&json"
    )

    print("\nSending request to:", url)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data:
            print("Currency not found. Try again.\n")
        else:
            print(f"\nExchange rate for {currency.upper()} for the last 7 days:\n")
            for item in data:
                print(item["exchangedate"], "-", item["rate"])
            print()
    else:
        print("Error! Status code:", response.status_code)
