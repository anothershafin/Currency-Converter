def get_valid_amount():
    while True:
        user_input = input("Enter the amount you want to convert (or press q to quit): ").strip()

        if user_input.lower() == "q":
            return "q"

        try:
            amount = float(user_input)
            if amount < 0:
                print("Amount cannot be negative. Please enter a valid amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_currency(prompt, valid_currencies):
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == "q":
            return "q"

        currency = user_input.upper()

        if currency in valid_currencies:
            return currency

        print("Invalid currency selection. Please try again.")


def ask_to_continue():
    while True:
        choice = input("Do you want to convert again? (y/n or q to quit): ").strip().lower()

        if choice in ["y", "n", "q"]:
            return choice

        print("Invalid choice. Please enter y, n, or q.")


def show_history(history):
    if not history:
        print("No conversions were made.")
        return

    print("\nSession Conversion History:")
    print("=" * 50)
    for i, record in enumerate(history, start=1):
        print(f"{i}. {record}")
    print("=" * 50)


def converter():
    exchange_rates={
        "USD": {"BDT": 100.0, "EUR": 0.85, "USD": 1.00},
        "BDT": {"USD": 0.01, "EUR": 0.0085, "BDT": 1.00},
        "EUR": {"USD": 1.18, "BDT": 117.65, "EUR": 1.00}
    }

    history = []

    print("Welcome to the Currency Converter!")
    print("You can convert between USD, BDT, and EUR.")
    print("Press q at any stage to quit.")
    print("=" * 50)

    while True:
        amount = get_valid_amount()
        if amount == "q":
            print("Exiting the program...")
            break

        from_currency = get_valid_currency(
            "Enter the currency you want to convert from (USD, BDT, EUR) or q to quit: ",
            exchange_rates.keys()
        )
        if from_currency == "q":
            print("Exiting the program...")
            break

        to_currency = get_valid_currency(
            "Enter the currency you want to convert to (USD, BDT, EUR) or q to quit: ",
            exchange_rates[from_currency].keys()
        )
        if to_currency == "q":
            print("Exiting the program...")
            break

        converted_amount=amount*exchange_rates[from_currency][to_currency]

        result = f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
        print(result)
        history.append(result)

        choice = ask_to_continue()
        if choice in ["n", "q"]:
            print("Exiting the program...")
            break

        print("-" * 50)

    show_history(history)
    print("Goodbye!")


if __name__ == "__main__":
    converter()