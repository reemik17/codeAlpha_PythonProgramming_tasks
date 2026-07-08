# Stock prices
stock_list = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "AMZN": 190,
    "GOOGL": 170
}

total_amount = 0
user_stocks = {}

# Display all stocks
def show_stocks():
    print("Available Stocks")
    for stock, price in stock_list.items():
        print(stock, "-", price)

# Buy a stock
def purchase_stock():
    global total_amount

    stock = input("Enter stock name: ").upper()

    if stock not in stock_list:
        print("Stock not available.")
        return

    quantity = int(input("Enter stock quantity: "))

    if quantity <= 0:
        print("Quantity should be greater than 0.")
        return

    if stock in user_stocks:
        user_stocks[stock]["quantity"] += quantity
    else:
        user_stocks[stock] = {
            "quantity": quantity,
            "cost": stock_list[stock]
        }

    amount = stock_list[stock] * quantity
    total_amount += amount

    print("Stock added successfully.")

# Display file
def display_file():
    print("File")

    if len(user_stocks) == 0:
        print("No stocks purchased.")
    else:
        for stock, details in user_stocks.items():
            print(stock, "- Quantity:", details["quantity"], "- Price:", details["cost"])

    print("\nTotal Investment =", total_amount)

# Save file
def save_file():
    with open("file.txt", "w") as file:
        for stock, details in user_stocks.items():
            file.write(f"{stock} - Quantity: {details['quantity']} - Price: {details['cost']}\n")

        file.write("----------------------\n")
        file.write(f"Total Investment = {total_amount}")

    print("File saved successfully.")

# Main Menu
while True:
    print("===== Stock Tracker =====")
    print("1. Display Stocks")
    print("2. Purchase Stock")
    print("3. Display File")
    print("4. Save File")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_stocks()
    elif choice == 2:
        purchase_stock()
    elif choice == 3:
        display_file()
    elif choice == 4:
        save_file()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid option.")

