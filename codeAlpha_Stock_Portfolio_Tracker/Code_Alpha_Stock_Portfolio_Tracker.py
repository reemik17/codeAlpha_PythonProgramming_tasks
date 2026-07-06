# Dictionary of stock prices
stock_price = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

total = 0

# User input
stock_number = int(input("Enter stock number: "))

for i in range(stock_number):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_price:

        # Validate quantity
        while True:
            stock_quantity = int(input("Enter quantity: "))

            if stock_quantity > 0:
                break
            else:
                print("Quantity must be greater than 0. Please try again.")

        # Calculate total investment
        total += stock_price[stock_name] * stock_quantity

    else:
        print("Stock not found!")

# Display total investment
print("Total Investment Value =", total)

# Save result into text file
with open("stock_tracker.txt", "w") as file:
    file.write(f"Total Investment Value = {total}")

print("Result saved in stock_tracker.txt")