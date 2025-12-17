from validator import (
    validate_amount,
    validate_category,
    validate_description,
    validate_date,
)
from file_handler import save_expense
from datetime import datetime

# ADD NEW EXPENSE

def add_expense(expense):
    amount = validate_amount()
    if amount is None:
        return

    category = validate_category()
    if category is None:
        return

    description = validate_description()
    if description is None:
        return

    date = validate_date()
    if date is None:
        return

    expense.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    })

    save_expense(expense)
    print("Expense added successfully!")

# View all expense

def view_all_expense(expense):
    if not expense:
        print("No expenses found.")
        return

    print("All Expenses")
    for i, exp in enumerate(expense, start=1):
        print(
            f"{i}. {exp['date']} | {exp['category']} | "
            f"{exp['amount']} | {exp['description']}"
        )

# View expense by category

def view_by_category(expense):
    if not expense:
        print("No expenses available.")
        return

    category = input("Enter category name: ").strip().lower()
    if not category:
        print("Category cannot be empty.")
        return

    print(f" Expenses in Category: {category} ===")
    found = False

    for i, exp in enumerate(expense, start=1):
        if exp["category"].lower() == category:
            print(
                f"{i}. {exp['date']} | {exp['category']} | "
                f"{exp['amount']} | {exp['description']}"
            )
            found = True

    if not found:
        print("No expenses found for this category.")

# Edit expense

def edit_expense(expense):
    if not expense:
        print("No expenses to edit.")
        return

    view_all_expense(expense)

    try:
        index = int(input("Enter expense number to edit: ")) - 1
        if index < 0 or index >= len(expense):
            print("Expense does not exist.")
            return
    except ValueError:
        print("Invalid input.")
        return

    exp = expense[index]

    print("Press Enter to keep existing value")

    choice = input(f"Change amount? (current: {exp['amount']}) (y/n): ").lower()
    if choice == "y":
        new_amount = validate_amount()
        if new_amount is not None:
            exp["amount"] = new_amount

    choice = input(f"Change category? (current: {exp['category']}) (y/n): ").lower()
    if choice == "y":
        new_category = validate_category()
        if new_category is not None:
            exp["category"] = new_category

    new_desc = input(f"Description ({exp['description']}): ").strip()
    if new_desc:
        exp["description"] = new_desc

    choice = input(f"Change date? (current: {exp['date']}) (y/n): ").lower()
    if choice == "y":
        new_date = validate_date()
        if new_date is not None:
            exp["date"] = new_date

    save_expense(expense)
    print("Expense updated successfully!")

# Delete expense

def delete_expense(expense):
    if not expense:
        print("No expenses to delete.")
        return

    view_all_expense(expense)

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if index < 0 or index >= len(expense):
            print("Expense does not exist.")
            return
    except ValueError:
        print("Invalid input.")
        return

    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm == "yes":
        expense.pop(index)
        save_expense(expense)
        print("Expense deleted successfully.")
    else:
        print("Delete cancelled.")

# Monthly summary

def monthly_summary(expense):
    if not expense:
        print("No expenses available.")
        return

    monthly_total = {}
    category_total = {}

    for exp in expense:
        month = exp["date"][3:]  # mm-yyyy
        monthly_total[month] = monthly_total.get(month, 0) + exp["amount"]
        category_total[exp["category"]] = (
            category_total.get(exp["category"], 0) + exp["amount"]
        )

    print("\n=== Monthly Summary ===")
    for month, total in monthly_total.items():
        print(f"{month}: {total}")

    highest = max(category_total, key=category_total.get)
    print(
        f"Highest Spending Category: {highest} -> "
        f"{category_total[highest]}"
    )
