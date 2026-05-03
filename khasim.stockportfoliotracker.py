def stock_tracker():
    print("📈 Stock Portfolio Tracker\n")

    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 2800,
        "MSFT": 320
    }

    portfolio = {}
    total_investment = 0

    while True:
        stock = input("Enter stock name (or 'done' to finish): ").upper().strip()
        
        if stock == "DONE":
            break
        
        if stock not in stock_prices:
            print("❌ Stock not available in price list.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    print("\n📊 Your Portfolio:")
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock} → {qty} shares × ${price} = ${value}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Optional: Save to file
    save = input("\nDo you want to save to file? (yes/no): ").lower()
    
    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                file.write(f"{stock}: {qty} shares = ${value}\n")
            file.write(f"\nTotal Investment: ${total_investment}")
        
        print("✅ Portfolio saved to portfolio.txt")

# Run the program
stock_tracker()