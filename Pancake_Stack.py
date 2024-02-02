#
# Implementation of a node that represents the state of a pancake stack
# for A2 Informed Search assignment.
#
# CS 131 - Artificial Intelligence
#
# Written by - Vivian Lau vlau02
# Last modified - 10/16/2023

import math

class PancakeStack:
    
    # Sets pancake stack as given and backward cost as number of flips given
    # flip is defined as flip used to get to current state
    # order is defined as the order it was entered into the queue
    def __init__(self, curStack, parentIn, numFlips, flipIn, orderIn):
        self.pancakeStack = curStack
        self.parent = parentIn
        self.backwardCost = numFlips
        self.flip = flipIn
        self.order = orderIn
        
    # Returns string version of pancake stack
    def __str__(self):
        return self.pancakeStack
    
    def __lt__(self, pancakeStackIn):
        if self.getCost() != pancakeStackIn.getCost():
            return self.getCost() < pancakeStackIn.getCost()
        else:
            return self.order < pancakeStackIn.order
    
    # Gets the size of pancake at given start and end indices
    def getPancake(self, start, end):
        if (self.pancakeStack == ''): # string is empty
            return -1
        elif (end == -1): # no end found
            return int(self.pancakeStack[start:])
        else:
            return int(self.pancakeStack[start:end])
        
    # Generates all sizes of pancakes in the current state of pancake stack
    def getAllPancakes(self):
        numPancakes = 1
        start = 0
        end = self.pancakeStack.find(',' , start+1) # find the next comma
        yield self.getPancake(start, end)
        
        while end != -1: # cannot find any more commas (no more pancakes)
            start = end+1
            end = self.pancakeStack.find(',' , start+1)
            numPancakes += 1
            yield self.getPancake(start, end)
    
    # Landmark heuristic function for forward cost of flipping pancakes
    # Assumes goal state has pancakes no more than n size and of n different sizes
    # Assumes adjacent pancakes in goal state does not differ in size more than 1
    def getForwardCost(self):
        forwardCost = 0
        
        pancakes = list(self.getAllPancakes())
        j = len(pancakes)
        for i in pancakes:
            if abs(i-j) > 1:
                forwardCost += 1
            j = i
                
        return forwardCost
    
    # Gets backward cost
    # Backward cost is how many pancakes were flipped to get to current stack
    def getBackwardCost(self):
        return self.backwardCost
    
    # Gets the total cost to get to the current pancake stack
    def getCost(self):
        return self.getForwardCost() + self.backwardCost
    
    def getFlip(self):
        if self.parent is None: # is root node
            return
        elif self.parent.getFlip() is None: # parent has no flips
            result = []
            result.append(self.flip)
            return result
        else:
            result = self.parent.getFlip()
            result.append(self.flip)
            return result
        
    # takes in index to flip at and returns flipped pancake stack
    def getFlippedChild(self, index):
        childPancakeStack = list(self.getAllPancakes())
        
        # runs through the portion of the pancake stack that needs to be flipped
        for pindex in range(0, math.floor((len(childPancakeStack)-index)/2)):
            pcake1 = index+pindex
            pcake2 = (len(childPancakeStack)-1-pindex)
            
            # swap the two elements as they are reflected into flipped stack
            temp = childPancakeStack[pcake1]
            childPancakeStack[pcake1] = childPancakeStack[pcake2]
            childPancakeStack[pcake2] = temp
            
        return ','.join(str(i) for i in childPancakeStack)
    
    # Returns all versions of pancake stack after flipping once (not including original)
    def possibleFlipChildren(self):
        nonFlipStack = list(self.getAllPancakes())
        
        flippedStack = []
        
        flipChildren = [None] * (len(nonFlipStack)-1)
        
        # flipping last pancake does not change stack
        flippedStack.append(nonFlipStack.pop())
        
        indexFlip = len(nonFlipStack)-1
        
        while len(nonFlipStack) != 0:
            flippedStack.append(nonFlipStack.pop())
            flipChildren[indexFlip] = ','.join(str(i) for i in list(nonFlipStack + flippedStack))
            indexFlip -= 1
        
        return flipChildren