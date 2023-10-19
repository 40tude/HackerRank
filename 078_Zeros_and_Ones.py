
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./078_Zeros_and_Ones_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given the shape of the array in the form of space-separated integers, 
# each integer representing the size of different dimensions, 
# your task is to print an array of the given shape 
# and integer type using the tools numpy.zeros and numpy.ones.



# In 
# A single line containing the space-separated integers.
# 1<=int<=3
# 3 3 3

# Out 
# First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.
# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]

if __name__ == '__main__':
  
  list_of_dim = list(map(int, input().split()))

  print(np.zeros(list_of_dim, dtype=int))
  print(np.ones (list_of_dim, dtype=int))
  CloseIO()