#
# A* search algorithm for A2 Informed Search assignment.
# CS 131 - Artificial Intelligence
#
# Written by - Vivian Lau vlau02
# Last modified - 10/16/2023

from Priority_Queue import PriorityQueue
from Pancake_Stack import PancakeStack

class AStarSearch:
    
    # Given the initial pancake stack as a list
    # makes a PancakeStack root node with empty states
    # also creates solution node for printing
    def __init__(self, initPStackIn):
        self.initPStack = PancakeStack(','.join(str(i) for i in initPStackIn), \
                                       None, 0, None, 0)
        self.solution = None
    
    # Uses A* search algorithm that prioritizes gap heuristics and number of
    # flips to narrow the search and find a solution
    # Returns list of flip orders if solution found and None if not
    def search(self):
        pq = PriorityQueue()
        pq.push(self.initPStack) # initial pancake stack state
        
        visited = []
        count = 1
        
        while(not(pq.empty())):
            curPStack = pq.get() # get next lowest cost pancake stack
            visited.append(curPStack.__str__()) # set current node to visited
            
            if curPStack.getForwardCost() == 0: # if reached goal state
                finalStack = list(curPStack.getAllPancakes())
                
                # check if pancake stack is reversed order and flip once more if so
                if (finalStack is not None and \
                    len(finalStack) > 1 and finalStack[0] < finalStack[1]):
                    self.solution = PancakeStack(curPStack.getFlippedChild(0), \
                                                 curPStack, \
                                                 curPStack.getBackwardCost()+1, \
                                                 0, count+1)
                else: # pancake stack is upright so just return
                    self.solution = curPStack
                return curPStack.getFlip() # returns all the flips done
            
            newFlip = 0
            # for each of the children of the current pancake stack
            for newFlipPStack in curPStack.possibleFlipChildren():
                child = PancakeStack(newFlipPStack, curPStack, \
                                     (curPStack.getBackwardCost()+1), \
                                     newFlip, count)
                
                # Checks if child is visited and not in queue
                if (not child.__str__() in visited) and (not pq.contains(child)):
                    pq.push(child) # pushes child
                else:
                    pq.replace(child) # replace child if has lower cost
                
                newFlip += 1
                
            count += 1
                
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
                    curPStack = PancakeStack(curPStack.getFlippedChild(i), curPStack, \
                                             curPStack.getBackwardCost()+1, i, 0)
                    print('\tPancake Stack now: ', curPStack.__str__())
        print()
        