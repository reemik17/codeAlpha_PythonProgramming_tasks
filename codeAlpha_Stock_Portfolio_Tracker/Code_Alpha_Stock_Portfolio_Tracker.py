# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "AMZN": 190,
    "GOOGL": 170
}

total_investment = 0

while True:
    print("===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. View Total Investment")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock_name = input("Enter stock name: ").upper()

        if stock_name in stock_prices:

            try:
                quantity = int(input("Enter stock quantity: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
                
            if quantity > 0:
                investment = stock_prices[stock_name] * quantity
                total_investment += investment
                print("Investment for", stock_name, "=", investment)
            else:
                print("Quantity must be greater than 0.")
                
        else:
            print("Stock not found.")

    elif choice == "2":
        print("Total Investment =", total_investment)

    elif choice == "3":
        break

    else:
        print("Invalid option. Please try again.")

# Save result to file
with open("file.txt", "w") as file:
    file.write(f"Total Investment = {total_investment}")

print("Result saved successfully.")
