# learning how to use nested loops
# 9/22/2019
# CTI-110 P4HW3 - Nested Loops
# Omar Roman JR
#

# This program displays a Stair-step pattern

for r in range (6):
    print("#", end="",sep="")
    for spaces in range(r):
        print(' ', end='', sep="")
    print("#")
