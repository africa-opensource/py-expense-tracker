import csv
project_name = "Ey Expense Tracker"
underline = "================================================"

def display_menu():
    print("Select your options")
    print(underline)
    print("1. View your expenses")
    print("2. Add your expenses")
    print("3. Update expenses")
    print("4. Exit expenses")

#Save the data we're about to collect
data = []

def add_expense():
    # Enter the number of expenses to be computed
    num_of_expenses = int(input("Enter the number of expenses to be computed: "))
    print(underline)
    #Request for the amount of each of the expenses
    for i in range(num_of_expenses):
                amount = float(input("Enter the amount of expense #{} in GHS: " .format(i + 1)))
                description = input("Enter category of expenses: ")
                date  = input("Enter date in this form dd/mm/yyyy: ")
                print(underline)
                data.append(amount)
                with open("expenses.txt", mode='w', newline='') as file:
                    writer = csv.writer(file) 
                    writer.writerow([description,amount,date])
    print("Expenses added successfully and the total sum is: GHS",sum(data))
    print(underline)
def main():
        print(project_name)
        print(underline)
        display_menu()
        print(underline)
        add_expense()

if __name__ == "__main__":
        main()



