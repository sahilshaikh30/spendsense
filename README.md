# SpendSense

A Python console script that takes a monthly budget and expenses for four categories, then prints a spending report with the remaining budget and budget status. Built as a beginner project to practice user input, arithmetic, conditionals, and formatted output.

## Features
- Enter a monthly budget and expenses for food, travel, shopping, and other
- Calculates total expense, average expense per category, and remaining budget
- Shows a budget status: Within Budget, Budget Fully Used, or Over Budget
- Prints a formatted report with amounts in ₹ to two decimal places

## Tech used
- Python 3
- Standard library only (no installs needed)

## How to run
1. Make sure Python 3 is installed
2. Download or clone this repo
3. Run:
   ```
   python spendsense.py
   ```
4. Enter your budget and expenses when prompted (whole numbers only)

## Sample output
```
============Spend Sense============
Monthly Spending Report
Monthly Budget: ₹20000.00
Food Expense: ₹6000.00
Travel Expense: ₹2500.00
Shopping Expense: ₹4000.00
Other Expense: ₹1500.00
Total Expense: ₹14000.00
Average Expense: ₹3500.00
Remaining Budget: ₹6000.00
Budget Status: Within Budget
====================================
```

## What I practiced
- Taking input with `input()` and converting it with `int()`
- Arithmetic and variables
- `if / elif / else` for budget status
- f-string formatting with two decimal places

## Known issues
- Typing text or a decimal instead of a whole number crashes the script
- Negative amounts are accepted without any check
- Data is not saved, so each run starts from scratch

## Planned improvements
- Validate input with `try/except`
- Allow decimal amounts
- Save monthly data to a CSV file or SQLite database
- Analyze spending over several months with pandas
