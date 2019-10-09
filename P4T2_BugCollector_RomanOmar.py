#Initialize the accumlator.
total = 0

#Get the bugs
for day in range(1, 8):
    #Prompt the user.
    print('Enter the bugs collected on day', day)

    #Input the number of bugs.
    bugs = int(input())

    #Add bugs to total
    total +=bugs


#Display the total bugs
print('you collected a total of', total, 'bugs.')
