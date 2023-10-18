# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true

import numpy # imposé !!!!
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./074_np_array_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# 1 2 3 4 -8 -10

# Out 
# [-10.  -8.   4.   3.   2.   1.]


def arrays(arr):                        # imposé !!!!!!!!!!
  my_list = list(map(float, arr))
  my_ndarray = numpy.array(my_list)
  my_ndarray=numpy.flip(my_ndarray)
  return my_ndarray

arr = input().strip().split(' ')    # imposé !!!!!!!!!!
result = arrays(arr)
print(result)
CloseIO()