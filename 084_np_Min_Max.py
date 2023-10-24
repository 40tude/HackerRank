
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./084_np_Min_Max_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a 2-D array with dimensions n x m
# Your task is to perform the min function over axis 1 and then find the max of that.
# The first line of input contains the space separated values of  and .
# The next  lines contains  space separated integers.

if __name__ == '__main__':
  
  n, m = map(int, input().split())
  A = np.empty((n, m), dtype=int)  
  for j in range(n):
    A[j,] = list (map(int, input().split()))
  
  print(np.max(np.min(A, axis=1)))
  CloseIO()