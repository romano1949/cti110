# Using def main and import random together
# 9/29/2019
# CTI-110 P5HW2 - Math Quiz Part 2
# Omar Roman Jr
#

import random

add_Numbers = 1
sub_Numbers = 2
exit_Numbers = 3

def main():
    
    choice = 0
    
#Begin the loop that will bring up the menu 
    
    while choice != exit_Numbers:
        
#Call the display menu function
        
        display_menu()
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            adding()
            
        elif choice == 2:
            subtracting()
            
        else:
            choice == 3
    

def adding():
    
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
            
def subtracting():
    
    number1 = random.randint(1,200)
    number2 = random.randint(1,200)
    
    correct = False
    
    while correct == False:
            
        print("What is " + str(number1) + " minus " + str(number2) + " ? ")
            
        a = int(input("Enter your answer: "))
        
        if a == number1-number2:
            correct = True
            print("Congratulations!")
            
        else:
            correct = True
            print("Wrong, the correct answer is: " + str(number1-number2))

def display_menu():
    
    print(" MAIN MENU")
    print("---------------")
    print("1) Add Random Numbers")
    print("2) Subtract Random Numbers")
    print("3)  Exit")
        
main()
