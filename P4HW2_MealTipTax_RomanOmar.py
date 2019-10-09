# CTI-110
# P4HW2 - MealTipTax
# Omar Roman Jr
# 9/22/2019
#

keepGoing = 'y'

while keepGoing == 'y':


    # How much the food cost
    meal = float ( input ('How much did your meal cost? '))
    print (' The original food charge is $', format (meal, ',.2f'))

    # Tip percentage
    tip = float(input('Enter the tip percentage '))
    print(' The tipAmount is $', format (tip, ',.2f'))

    # Tax amount
    tax = meal* .06
    print (' The taxAmount is $', format (tax, ',.2f'))

    if tip == .16:
        print(tip)
    elif tip == .18:
        print (tip)
    elif tip == .20:
        print (tip)
    else:
        print ('Error: Enter tip again for (i.e 0.18 for 18%) ')

        tip = float(input('Enter the tip percentage'))
        print(' The tipAmount is $', format (tip, ',.2f'))

    tip = tip
    # Tip amount
    tipAmount = meal * tip        
        
    #Calculate the total cost.
    total_cost = meal + tax + tipAmount

    #all the amounts
    print (' The original food charge is $', format (meal, ',.2f'))
    print(' The tipAmount is $', format (tip, ',.2f'))
    print (' The taxAmount is $', format (tax, ',.2f'))
    print('Your total meal cost is: $ %.2f' % total_cost )

    #Run again?
    keepGoing = input('Do you want to enter another tip (Enter y for yes)')
