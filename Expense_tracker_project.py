import csv
import os
from datetime import datetime

# Initialize an empty list to store expenses and define global variable
expenses = []
csv_storage_file = "Expense_data.csv"
CATEGORIES = {"F": "Food", "T": "Travel","B":"Bills","M":"Miscellaneous"}
date_format = "%Y-%m-%d"
fieldnames = ['date', 'category', 'amount', 'description']


# validate date and get input for date from users
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date frmat. Please enter the date in yyyy-mm-dd format")
        return get_date(prompt, allow_default)

# validate amount entered for budget.
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

# validate amount entered for budget.
def get_budget():
    try:
        amount = float(input("Enter your monthly budget: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

#get transaction description for entered expense.        
def get_description():
    desc = input("Enter a description: ").strip()
    if not desc:
        print("please enter Description")
        get_description()
    else:
        return desc

# validate category and get input for category from users    
def get_category():
    category = input("Enter the category ('F': 'Food' or 'T': 'Travel' or 'B':'Bills' or 'M':'Miscellaneous.'").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please Enter the category ('F': 'Food' or 'T': 'Travel' or 'B':'Bills' or 'M':'Miscellaneous'.")
    return get_category()


# Load expenses from a CSV file at startup
def load_expenses():
    global expenses
    if os.path.exists(csv_storage_file):
        with open(csv_storage_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            expenses = [dict(row) for row in csv_reader]

# Save expenses to a CSV file
def save_expenses():
    global expenses
    global fieldnames
    if not expenses:
       print("There is no data or data already saved. Please check")
    else: 
        with open(csv_storage_file, mode='w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(expenses)
        expenses = []   
        load_expenses ()

# Function to add an expense and store in dictionary 
def add_expense():
    date = get_date(
        "Enter the date of the transaction (yyyy-mm-dd) or enter for today's date: ",
        allow_default=True,
    )
    category = get_category()
    amount = get_amount()
    description = get_description()

    # Validate inputs
    if not all([date, category, amount, description]):
        print("Incomplete expense details. Please provide all information.")
        return

    try:
        # Convert amount to float and validate date
        amount = float(amount)
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid input. Please ensure the amount is a number and the date is in the correct format.")
        return
    # Add the expense to the list
    expenses.append({'date': date, 'category': category, 'amount': amount, 'description': description})
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    global expenses
    if not expenses:
        print("No expenses recorded yet.")
        return    
    print("Below are expense captured.")
    for entry in expenses:
        if all(entry.values()):  # Check if all fields are present
            print(f"Date: {entry['date']}, Category: {entry['category']}, Amount: {entry['amount']}, Description: {entry['description']}")
        else:
            print("Incomplete entry found, skipping.")

# Function to track the budget
def track_budget():
    budget = get_budget()
    total_expenses = sum(float(entry['amount']) for entry in expenses)
    
    if total_expenses > budget:
        print(f"You have exceeded your budget! Total expenses: {total_expenses}, Budget: {budget}")
    else:
        remaining = budget - total_expenses
        print(f"You have {remaining} left for the month.")

# Function to display the menu
def menu():
    load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            if not expenses:
                print("There is no data save. Please check")
            else:
                save_expenses()
                print("Expenses saved successfully.")
        elif choice == '5':
            if not expenses:
                print(f"Exiting program. Goodbye! {individual_name}")
                break
            else:
                save_expenses()
                print("Data saved Exiting program. Goodbye!")
                break
        else:
            print("Invalid option. Please choose again.")

# Main program
if __name__ == "__main__":
    menu()
