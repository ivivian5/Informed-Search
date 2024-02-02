#
# Implementation of a priority queue for prioritization of pancake stacks
# for the A2 Informed Search assignment.
# CS 131 - Artificial Intelligence
#
# Written by - Vivian Lau vlau02
# Last modified - 10/15/2023

from queue import PriorityQueue
import heapq

class PriorityQueue(PriorityQueue):
    
    # Creates empty heap (represented by list)
    def __init__(self):
        self.heap = []
    
    # Returns if the priority queue is currently empty
    def empty(self):
        return len(self.heap) == 0
    
    # Returns size of pq
    def size(self):
        return len(self.heap)

    # Gets and removes the next pancake stack with least cost
    def get(self):
        return heapq.heappop(self.heap)
    
    # Takes in a version of the pancake stack to push onto the heap
    # Prioritizes first by cost of pancake stack being lesser
    def push(self, pstackIn):
        heapq.heappush(self.heap, pstackIn)
    
    # Checks if pancake stack is currently in the priority queue
    # returns True if so
    def contains(self, pstackIn):
        for i in self.heap:
            if i.__str__() == pstackIn.__str__():
                return True
        return False
    
    # If given pancake stack has a lower cost and in the priority queue, 
    # replace old with given
    # Returns True if successful and False if not
    def replace(self, pstackIn):
        for i in self.heap:
            if i.__str__() == pstackIn.__str__() and i.getCost() > pstackIn.getCost():
                self.heap[self.heap.index(i)] = pstackIn
                return True
        return False