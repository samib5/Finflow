while True:
    try:
        income = round(float(input("What's your monthly income ? ")), 2)
    except ValueError:
        print("Please enter a valid number.")
    else:
        if income < 0:
            print("Income cannot be negative.")   
        else:
            break
print(f"Your monthly income is ${income:.2f}")

while True:
    try:
        number_of_expenses = int(input("How many expenses do you want to add ? "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        if number_of_expenses < 0:
            print("Number of expenses cannot be negative.")
        else:   
            break
expenses = []

for i in range(number_of_expenses):
    while True:
        try:
            expense = round(float(input(f"Expense {i + 1} ? ")), 2)
        except ValueError:
            print("Please enter a valid number.")
        else:
            if expense < 0:
                print("Expense cannot be negative.")
            else:
                break
    expenses.append(expense)

total_expenses = round(sum(expenses), 2)
balance = round(income - total_expenses, 2)
print(f"Your total expenses are ${total_expenses:.2f}")
print(f"Your balance is ${balance:.2f}")
