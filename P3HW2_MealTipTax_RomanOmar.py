# CTI-110
# P3HW2 - MealTipTax
# Omar Roman Jr 
# 9/11/2019
#

# How much the food cost.
meal = float( input ('How much did your meal cost? '))
print (' The original food charge is $', format (meal, ',.2f'))

# Tax amount
tax = meal * .06
print (' The taxAmount is $', format (tax, ',.2f'))

# Tip percentage
tip = float(input('Enter the tip percentage'))
print(' The tipAmount is $', format (tip, ',.2f'))

if tip == .16:
    print(tip)
elif tip == .18:
    print (tip)
elif tip == .20:
    print (tip)
else:
    print ('Error defaulting to .16')
    tip = .16
# Tip amount
tipAmount = meal * tip        
    
#Calculate the total cost.
total_cost = meal + tax + tipAmount
print('Your total meal cost is: $ %.2f' % total_cost)

