# We are calculating the total including tax and tip
# 9/2/2019
# CTI-110 P2HW1- Meal Tip Tax Calculator
# Omar Roman Jr
#


# How much the food cost. 
meal= float(input('How much did your meal cost? '))

# How much the customer tips.
tipAmount= float ( input(' Enter the tip percentage'))

# How much the customer taxed
taxAmount= float ( input(' Enter the tax percentage'))

# Calculate the tip.
tip = meal * tipAmount
print (' The tipAmount is $', format (tip, ',.2f'))

#Calculate the tax.
tax = meal * taxAmount
print (' The taxAmount is $', format (tax, ',.2f'))

#Calculate the total cost.
total_cost = meal + tax + tip
print('Your total meal cost is: $ %.2f' % total_cost)
