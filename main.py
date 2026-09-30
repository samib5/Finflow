income = int(input("What's your monthly income ? "))
print(f"Your monthly income is ${income}")
x = int(input("How many expenses do you want to add ? "))
expenses = []
for i in range(x):
    expense = round(float(input("Expense ? ")), 2)
    expenses.append(expense)
total_expenses = round(sum(expenses), 2)
balance = round(income - total_expenses, 2)
print(f"Your total expenses are ${total_expenses:.2f}")
print(f"Your balance is ${balance:.2f}")
