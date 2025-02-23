
# In Python, an important thing to know is that the same type of quote used to define a string cannot be used inside it. For example, the string 'I'm a string!' is not valid. To use the single quote inside that string you should either:

# Escape the quote by prepending a backlash to it: 'I\'m a string!'
# Or use double quotes to define the string: "I'm a string!" (preferred).
# You can access values in a dictionary through its keys. You need to use bracket notation and include the key between the square brackets:

# Example Code
# my_dict = {'amount': 50.0, 'category': 'Food'}
# my_dict['amount'] # 50.0
# You are currently interpolating the expense dictionary in your f-string. Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.

# def add_expense(expenses, amount, category):
#     expenses.append({'amount': amount, 'category': category})
    
# def print_expenses(expenses):
#     for expense in expenses:
#         print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# expenses = []



def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()