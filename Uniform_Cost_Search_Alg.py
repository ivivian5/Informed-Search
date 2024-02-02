#
# Uniform Cost search algorithm for A2 Informed Search assignment
# Also includes PancakeStack class wrapper to override getCost function
# CS 131 - Artificial Intelligence
#
# Written by - Vivian Lau vlau02
# Last modified - 10/16/2023

from Priority_Queue import PriorityQueue
from Pancake_Stack import PancakeStack

class SimplePStack(PancakeStack):
    def getCost(self):
        return self.backwardCost

class UniformCostSearch:
    
    # Given the initial pancake stack as a list
    # creates a SimplePStack root node with empty states
    # also creates solution node for printing 
    #              and goalState string to find solution
    def __init__(self, initPStackIn):
        self.initPStack = SimplePStack(','.join(str(i) for i in initPStackIn), \
                                       None, 0, None, 0)
        self.solution = None
        self.goalState = ''
    
    # Sets an end goal state to compare with when reach solution
    def setGoalState(self):
        pStack = list(self.initPStack.getAllPancakes())
        minP = min(pStack)
        self.goalState = ','.join(str(i) for i in \
                                  reversed(range(minP, minP+len(pStack))))
    
    # Uses uniform cost search algorithm that prioritizes cost of each flip
    # to find a solution
    # Returns list of flip orders if solution found and None if not
    def search(self):
        #initialize problem state
        self.setGoalState()
        pq = PriorityQueue()
        pq.push(self.initPStack) # initial pancake stack state
        
        visited = []
        count = 1
        
        while(not(pq.empty())):
            curPStack = pq.get() # get next lowest cost pancake stack
            visited.append(curPStack.__str__()) # set visited to true
            
            if curPStack.__str__() == self.goalState: # if reached goal state
                self.solution = curPStack
                return curPStack.getFlip() # returns all the flips done
            
            newFlip = 0
            # for each of the children of the current pancake stack
            for newFlipPStack in curPStack.possibleFlipChildren():
                child = SimplePStack(newFlipPStack, curPStack, \
                                     (curPStack.getBackwardCost()+1), \
                                     newFlip, count)
                
                # Checks if child is visited and not in queue
                if (not child.__str__() in visited) and (not pq.contains(child)):
                    pq.push(child) # pushes child
                else:
                    pq.replace(child) # replacing child if has lower cost
                
                newFlip += 1
                
            if(pq.empty()): # if no more child nodes, then failed
                return None
            
    # Assumes that search function has already ran search()
    # Prints solution if one is found
    def printPath(self):
        if self.solution is None: #Solution is not found
            print('\nNo Solution Found! Please try running a different', \
                  'pancake stack with the search() function!')
        else:
            curPStack = self.initPStack
            count = 1
            print('\nPancake Stack start: ', curPStack.__str__(), '\n')
            
            if self.solution.getFlip() is None:
                print('No flips needed!')
            else:
                for i in self.solution.getFlip():
                    print('Step ', str(count), ': Flip under pancake ', str(i))
                    count += 1
                    curPStack = SimplePStack(curPStack.getFlippedChild(i), curPStack, \
                                             curPStack.getBackwardCost()+1, i, count)
                    print('\tPancake Stack now: ', curPStack.__str__())
        print()
        