# Personal_Expense_tracker
Personal_Expense_tracker

Overview
This Personal Expense Tracker is a simple command-line application designed to help users manage their expenses. It allows users to add, view, and track their expenses while saving them in a CSV file for later reference.

Features
- Add Expense: Input date, category, amount, and description for an expense.
- View Expenses: Display all recorded expenses.
- Track Budget: Compare total expenses against a user-defined budget.
- Save Expenses: Save all recorded expenses to a CSV file for future access.
- Load Expenses: Automatically load previously saved expenses upon startup.

  Menu Options
1. Add Expense: Add a new expense by providing date, category, amount, and description.
2. View Expenses: Display all expenses captured.
3. Track Budget: Enter your monthly budget to see if you are within limits.
4. Save Expenses: Save your current expenses to a CSV file.
5. Exit: Save and exit the program.

Input Formats
- Date: Format must be `yyyy-mm-dd`. You can press enter to use today's date.
- Category: Enter one of the following:
  - `F`: Food
  - `T`: Travel
  - `B`: Bills
  - `M`: Miscellaneous
- Amount: Must be a positive number.
- Description: A brief note about the expense.

Data Storage
Expenses are stored in a CSV file named `Expense_data.csv`. This file is created in the same directory as the script. Each expense is recorded with the following fields:
- Date
- Category
- Amount
- Description

Notes
- Ensure to provide all required information when adding an expense.
- The program will prompt you if any input is invalid or missing.
