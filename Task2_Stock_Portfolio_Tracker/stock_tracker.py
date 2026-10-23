# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

import csv

# Hardcoded stock prices (educational example)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}


def display_stocks():
    """Display available stocks and their prices."""
    print("\n========== AVAILABLE STOCKS ==========")
    print(f"{'Stock':<15}{'Price ($)':>12}")
    print("-" * 27)

    for stock, price in stock_prices.items():
        print(f"{stock:<15}{price:>12.2f}")

    print("=" * 39)


def calculate_portfolio(portfolio):
    """Calculate the total investment value."""
    total = 0

    for stock, quantity in portfolio.items():
        total += stock_prices[stock] * quantity

    return total


def display_portfolio(portfolio):
    """Display the user's portfolio and total investment."""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n========== YOUR PORTFOLIO ==========")
    print(f"{'Stock':<15}{'Quantity':>12}{'Price ($)':>15}{'Value ($)':>15}")
    print("-" * 57)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        print(
            f"{stock:<15}{quantity:>12}"
            f"{price:>15.2f}{value:>15.2f}"
        )

    print("-" * 57)
    print(f"{'TOTAL INVESTMENT:':<42}${calculate_portfolio(portfolio):,.2f}")
    print("=" * 57)


def save_portfolio(portfolio):
    """Save portfolio details to a CSV file."""
    if not portfolio:
        print("\nNothing to save. Your portfolio is empty.")
        return

    filename = "portfolio.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Stock",
                "Quantity",
                "Price ($)",
                "Investment Value ($)"
            ])

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                writer.writerow([
                    stock,
                    quantity,
                    price,
                    price * quantity
                ])

            writer.writerow([])
            writer.writerow([
                "TOTAL",
                "",
                "",
                calculate_portfolio(portfolio)
            ])

        print(f"\nPortfolio saved successfully to {filename}!")

    except OSError as error:
        print(f"\nCould not save portfolio: {error}")


def main():
    """Run the Stock Portfolio Tracker."""
    portfolio = {}

    print("\n" + "=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("          CodeAlpha Task 2")
    print("=" * 45)

    while True:
        print("\n1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View Portfolio")
        print("4. Save Portfolio to CSV")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_stocks()

        elif choice == "2":
            display_stocks()

            stock = input(
                "\nEnter the stock symbol you want to add: "
            ).strip().upper()

            if stock not in stock_prices:
                print("Invalid stock symbol. Please choose an available stock.")
                continue

            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")
                continue

            portfolio[stock] = portfolio.get(stock, 0) + quantity

            print(f"\nAdded {quantity} shares of {stock} successfully!")

        elif choice == "3":
            display_portfolio(portfolio)

        elif choice == "4":
            save_portfolio(portfolio)

        elif choice == "5":
            print("\nThank you for using Stock Portfolio Tracker!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
