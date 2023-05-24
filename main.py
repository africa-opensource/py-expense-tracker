import csv
from terminaltables import AsciiTable
project_name = "Ey Expense Tracker"
underline = "=============================================================="

def display_menu():
    print("Select your options")
    print(underline)
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Update expenses")
    print("4. Delete expenses")
    print("5. Exit expenses ")

def add_expense():
    #Request for the details of each of the expenses
    amount = float(input("Enter the amount of expense in GHS: "))
    description = input("Enter category of expense: ")
    date  = input("Enter date in this form dd/mm/yyyy: ")
    print(underline)
    data = [description,amount,date]
    table = AsciiTable([["Description","Amount(GHS)","Date"],data])
    print(table.table)
    yes_or_no = input("Are you sure you want to add this expenses(Yes(y)/No(n)): ")
    if yes_or_no in ["yes","Yes","y","Y","YES"]:
        with open("expenses.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([description, amount, date])
        print("Expenses added successfully.")
    else:
         print("Add expense Unsuccessful.")
    print(underline)
def view_expense():
    #View your expenses
    data = [["Description","Amount(GHS)","Date"]]
    with open("expenses.csv",mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        if len(expenses) == 0:
            print("No Expenses to display")
        else:
            print("Your Expense Summary")
        for expense in expenses:
            data.append(expense)
        table = AsciiTable(data)
        print(table.table)
        print(underline)
def update_expense():
    description_key = input("Enter the key to search for the expense you want to update: ")
    amount_key = float(input("Enter it's corresponding amount in (GHS): "))
    print(underline)
    data = [["Description","Amount(GHS)","Date"]]

    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    expense_found = False
    for expense in expenses:
        if expense[0] == description_key and float(expense[1]) == amount_key:
            expense[1] = float(input("Enter the new amount of expense in (GHS): "))
            expense[0] = input("Enter the new category of expense: ")
            expense[2] = input("Enter the new date in this form dd/mm/yyyy: ")
            print(underline)
            expense_found = True
            data.append(expense)
            table = AsciiTable(data)
            print(table.table)
            yes_or_no = input("Are you sure you want to update this expenses(Yes(y)/No(n)): ")
            break
    else:
        print("Expense Not Found")
    if expense_found and (yes_or_no in ["yes","Yes","y","Y","YES"]):
        with open("expenses.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expenses Updated Successfully.")
    else:
        print("Expense Update Unsuccessful.")
    print(underline)
def delete_expense():
    #Delete Expense Option
    description_key = input("Enter the key to search for the expense you want to delete: ")
    amount_key = float(input("Enter it's corresponding amount in (GHS): "))
    print(underline)
    data = [["Description","Amount(GHS)","Date"]]

    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    expense_found = False
    for expense in expenses:
        if expense[0] == description_key and float(expense[1]) == amount_key:
            expense_found = True
            expenses.remove(expense)
            data.append(expense)
            table = AsciiTable(data)
            print(table.table)

            yes_or_no = input("Are you sure you want to delete this expenses(Yes(y)/No(n)): ")
            break
    else:
        print("Expense not found.")
    if expense_found and yes_or_no in ["YES","y","yes","Yes"]:
        with open("expenses.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expense Deleted Successfully")
    else:
        print(underline)
        print("Expense Delete Unsuccessful... ")
    print(underline)
def exit_expense():
    print("Exited successfully!.")
    print(underline)

def main():
    print(project_name)
    print(underline)
    display_menu()
    print(underline)
    option = 0
    while option != 5:
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
            print("Update Expenses Option")
            print(underline)
            update_expense()
        elif option == 4:
            print("Delete Expense Option")
            print(underline)
            delete_expense()
        elif option == 5:
            print("Exit Expenses Option") 
            print(underline)
            exit_expense()
        else :
            print("Invalid Option try another option.")
            print(underline)

if __name__ == "__main__":
        main()



