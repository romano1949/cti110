# Learning how to use import random
# 9/29/2019
# CTI-110 P5HW2 - Math Quiz Part 1
# Omar Roman Jr
#

import random

number1 = random.randint(1,200)
number2 = random.randint(1,200)

correct = False

while correct == False:
        
    print("What is " + str(number1) + " plus " + str(number2) + " ? ")
        
    a = int(input("Enter your answer: "))
    
    if a == number1+number2:
        correct = True
        print("Congratulations!")
        
    else:
        correct = True
        print("Wrong, the correct answer is: " + str(number1+number2))
        
