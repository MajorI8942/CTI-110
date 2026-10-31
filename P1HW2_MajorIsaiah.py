# Isaiah Major
# October 31, 2026
# P1HW2 - Travel Expense Calculator
# This program calculates travel expenses and subtracts
# them from the user's starting budget.

# Pseudocode:
# 1. Ask the user for their travel budget.
# 2. Ask the user for their travel destination.
# 3. Ask how much they will spend on gas.
# 4. Ask how much they will spend on accommodation.
# 5. Ask how much they will spend on food.
# 6. Add all travel expenses together.
# 7. Subtract total expenses from the budget.
# 8. Display the travel budget summary.

# Collect the user's travel information.
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

# Collect the estimated travel expenses.
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Add the expenses and calculate the remaining budget.
total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

# Display the travel expense summary.
print()
print("------------Travel Expenses------------")
print("Location:", destination)
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print("---------------------------------------")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_budget:.2f}")
