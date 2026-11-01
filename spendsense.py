# ---------------- GET MONTHLY BUDGET AND EXPENSES ----------------

# Ask the user to enter their monthly budget
monthly_budget = int(input("Enter monthly budget(in Rs): "))

# Take expenses for each category from the user
food_exp = int(input("Enter food expense(in Rs): "))
travel_exp = int(input("Enter travel expense(in Rs): "))
shopping_exp = int(input("Enter shopping expense(in Rs): "))
other_exp = int(input("Enter other expense(in Rs): "))


# ---------------- CALCULATE EXPENSES ----------------

# Add all four expenses to calculate total spending
total_exp = (food_exp) + (travel_exp) + (shopping_exp) + (other_exp)

# Calculate the money left after deducting expenses from budget
remaining_budget = monthly_budget - total_exp

# Calculate average expense across the four categories
avg_exp = total_exp / 4


# ---------------- CHECK BUDGET STATUS ----------------

# Check whether total expenses are less than the monthly budget
if total_exp < monthly_budget:
  budget_status = "Within Budget"

# Check whether the entire monthly budget has been used
elif total_exp == monthly_budget:
  budget_status = "Budget Fully Used"

# If neither condition is true, expenses have exceeded the budget
else:
  budget_status = "Over Budget"


# ---------------- DISPLAY MONTHLY REPORT ----------------

# Display the complete spending report with amounts formatted to 2 decimal places
print(f'''
============Spend Sense============
Monthly Spending Report
Monthly Budget: ₹{monthly_budget:.2f}
Food Expense: ₹{food_exp:.2f}
Travel Expense: ₹{travel_exp:.2f}
Shopping Expense: ₹{shopping_exp:.2f}
Other Expense: ₹{other_exp:.2f}
Total Expense: ₹{total_exp:.2f}
Average Expense: ₹{avg_exp:.2f}
Remaining Budget: ₹{remaining_budget:.2f}
Budget Status: {budget_status}
========================
''')