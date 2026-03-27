# Currency Converter

A simple Python-based currency converter that allows users to convert between multiple currencies with input validation, repeat conversion support, quit-anytime functionality, and session history tracking.

## Features

- Convert between **USD**, **BDT**, and **EUR**
- Input validation for amount and currency codes
- Prevents negative amount input
- Allows the user to quit at any stage by pressing `q`
- Supports multiple conversions in one run
- Stores and displays **session conversion history** before exit

## Technologies Used

- **Python 3**

## How It Works

The program:

1. Takes an amount from the user
2. Takes source and target currencies
3. Validates all inputs properly
4. Converts the amount using predefined exchange rates
5. Stores the conversion result in session history
6. Asks the user whether they want to convert again
7. Shows full session history before exiting

## Project Structure

```bash
currency_converter.py
README.md
```

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this project.
3. Open the project folder in terminal or VS Code.
4. Run the following command:

```bash
python currency_converter.py
```

## Example Run

```text
Welcome to the Currency Converter!
You can convert between USD, BDT, and EUR.
Press q at any stage to quit.
==================================================
Enter the amount you want to convert (or press q to quit): 100
Enter the currency you want to convert from (USD, BDT, EUR) or q to quit: USD
Enter the currency you want to convert to (USD, BDT, EUR) or q to quit: BDT
100.00 USD is equal to 10000.00 BDT
Do you want to convert again? (y/n or q to quit): n
```

## Learning Outcomes

This project helped practice:

- Functions in Python
- Loops and conditional statements
- Dictionary usage
- Input validation
- Modular code structure
- Basic user interaction in terminal programs

## Future Improvements

- Add more currencies
- Use real-time exchange rates from an API
- Add date and time to conversion history
- Build a GUI version using Tkinter



This is a beginner-friendly Python project made for practice and learning.
