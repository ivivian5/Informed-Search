#
# main for running the A2 Informed Search assignment.
# CS 131 - Artificial Intelligence
#
# Written by - Vivian Lau vlau02
# Last modified - 10/16/2023

import random
import timeit
from numpy.random import shuffle # randomly shuffle sequence (for testing)
from Pancake_Stack import PancakeStack
from A_Star_Search_Alg import AStarSearch
from Uniform_Cost_Search_Alg import UniformCostSearch


done = False
pancakes = []

print("Please enter a valid pancake stack with sequential values",\
      "to be flipped back into order from largest to smallest.")

while not done:
    userInput = input ('Enter an integer representing pancake'+\
                       ' size (and done if no more): ')
    if userInput.lower() == 'done':
        done = True
    else:
        try:
            userInput = int(userInput)
            pancakes.append(userInput)
        except ValueError:
            print ('Please give a valid integer.')

# pancake of sizes from 1 to 10
#pancakes = [i for i in range(1,11)]
# randomly shuffle the pancakes to create problem pancake stack
#shuffle(pancakes)

astar = AStarSearch(pancakes)

#run A* algorithm to see if there is solution
timerStart = timeit.default_timer()
astar.search()
timerEnd = timeit.default_timer()

# print results
print ("With A* Search Algorithm: ")
print("Execution Time:", round(timerEnd - timerStart, 3), " seconds")
astar.printPath()

# Uniform Cost Search to be done if less than 8 pancakes (takes too long)
if (len(pancakes) < 8):
    ucs = UniformCostSearch(pancakes)

    #run A* algorithm to see if there is solution
    timerStart = timeit.default_timer()
    ucs.search()
    timerEnd = timeit.default_timer()

    print ("With Uniform Cost Search Algorithm: ")
    # print results
    print("Execution Time:", round(timerEnd - timerStart, 3), " seconds")
    ucs.printPath()