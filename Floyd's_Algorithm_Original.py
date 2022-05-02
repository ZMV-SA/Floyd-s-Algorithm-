#This is the original code implementation which has been updated to PEP8 standard

import datetime #used to determine the  runtime as part of compartive performative testing

start_time =datetime.datetime.now() #initiate timestamp before starting of function

import sys # used to check the largest int size for infinite distiances  
import itertools 

NO_PATH = sys.maxsize # used for the infite size distances 
graph = [[0, 7, NO_PATH, 8], # This is the assignement input matrix 
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


def floyd(distance):
#"""
#A simple implementation of Floyd's algorithm
#"""
    for intermediate, start_node,end_node in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
            if start_node == end_node:
                distance[start_node][end_node] = 0
                continue
            #return all possible paths and find the minimum
            distance[start_node][end_node] = min(distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node] )
        #Any value that have sys.maxsize has no path
    print (distance)
floyd(graph)

end_time=datetime.datetime.now() #end time stamp one algorith has completed running 
print ("the Algorithm runtime is \n")
print (end_time-start_time)  # print algorithm runtime 