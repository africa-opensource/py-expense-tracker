import csv
project_name = "Ey Expense Tracker"
underline = "================================================"

def display_menu():
    print("Select your options")
    print(underline)
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Update expenses")
    print("4. Exit expenses")

def add_expense():
    #Request for the details of each of the expenses
    amount = float(input("Enter the amount of expense in GHS: "))
    description = input("Enter category of expense: ")
    date  = input("Enter date in this form dd/mm/yyyy: ")
    print(underline)
    print("Description: ",description)
    print("Amount(GHS): ",amount)
    print("Date: ",date)
    print(underline)
    yes_or_no = input("Are you sure you want to add expenses: ")
    if yes_or_no == "yes" or "Yes" or "y" or "Y" or "YES":
        with open("expenses.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([description, amount, date])
        print("Expenses added successfully")
    else:
         print("Aborted")
    print(underline)
def view_expense():
    #View your expenses
    with open("expenses.csv",mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        if len(expenses) == 0:
            print("No Expenses to display")
        else:
            print("Your Expense Summary")
        for expense in expenses:
            print(f"Description: {expense[0]},\t\t Amount(GHS): {expense[1]},\t\t Date: {expense[2]}")
def update_expense():
    #Update your expenses using description key
    description_key = input("Enter a key to search for expense you want to update: ") 
    amount_key = float(input("Enter an amount to search for the amount you want to update: "))
    with open("expenses.csv",mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    expense_found = False
    for expense in expenses:
        if expense[0] == description_key and expense[1] == str(amount_key):
            expense_found = True
            new_amount = float(input("Enter the new amount of expense in GHS: "))
            new_description = input("Enter the new category of expense: ")
            new_date = input("Enter the new date in this form dd/mm/yyyy: ")
            print("Description: ",new_description)
            print("Amount: ",new_amount)
            print("Date: ",new_date)
            print("Expense  updated successfully.")
            with open("expenses.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)
        break
    if not expense_found:
        print("Expense  not found.")

def main():
    print(project_name)
    print(underline)
    display_menu()
    print(underline)
    option = 0
    while option != 4:
        option = int(input("Choose your option: "))
        if option == 1:
            print("Add Expenses Option")
            print(underline)
            add_expense()
        elif option == 2:
            print("View Expenses Option")
            print(underline) 
            view_expense()
        elif option == 3:
              print("Update Expenses")
              print(underline)
              update_expense()
        elif option == 4:
              print("Exit Expenses") 
        else :
              print("Invalid Option")


if __name__ == "__main__":
        main()



