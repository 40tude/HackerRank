# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./075_np_Shape_Reshape_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a space separated list of nine integers. 
# Your task is to convert this list into a X NumPy array.


# In 
# 1 2 3 4 5 6 7 8 9

# Out 
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


if __name__ == '__main__':
  lst = list(map(int, input().strip().split(' ')))
  my_array = np.array(lst)
  my_array = my_array.reshape(3,3)
  print (my_array)
  CloseIO()

  

