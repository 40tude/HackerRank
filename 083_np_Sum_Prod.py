
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./083_np_Sum_Prod_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a 2-D array with dimensions n x m
# Your task is to perform the sum tool over axis 0 and then find the product of that result.
# The first line of input contains space separated values of n and m.
# The next n lines contains m space separated integers.

# In 
# 2 2
# 1 2
# 3 4

# Out 
# 24

if __name__ == '__main__':
  
  n, m = map(int, input().split())
  A = np.empty((n, m), dtype=int)  
  for j in range(n):
    A[j,] = list (map(int, input().split()))
  
  # B = A.sum(axis=0)
  # print(B)
  # print(B.prod())
  # print(A.sum(axis=0))
  print(A.sum(axis=0).prod())

  CloseIO()