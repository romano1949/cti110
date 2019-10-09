# CTI-110
# P4HW1 - Expenses
# Omar Roman Jr
# 9/22/2019

keepgoing = 'y'

while keepgoing == 'y':


    #How much withdrawn
    account = float( input('How much money is in the account? '))

    titleExpense = input (' What it the name of the first expense? ')

    amountExpense = float( input(' How much did the first expense cost? '))

    finalBalance = account - amountExpense

    print(' The final balance is $', format (finalBalance, ',.2f'))

    keepgoing = input('Do you want to enter another expense(Enter y for yes)')

    print(f'{"Amount":<6}{"Expense":<8}')

    print ('Amount in account before expense subtraction:', + account )

    print ('-----------------------------')

    print ('    Expense Calculator')

    print ('-----------------------------')
