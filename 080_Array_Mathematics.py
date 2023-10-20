import numpy as np

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./080_Array_Mathematics_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 
# The first line contains two space separated integers, N and M
# The next N lines contains M space separated integers of array A
# The following N lines contains M space separated integers of array B
# Your task is to ...

# Out 
# Add the 2 matrces 
# Subtract 
# Multiply 
# Integer Division 
# Mod 
# Power 

if __name__ == '__main__':

  n, m = map(int, input().split())
  A = np.empty((n, m), dtype=int)  
  B = np.empty((n, m), dtype=int)  
  for j in range(n):
    A[j,] = list (map(int, input().split()))
  for j in range(n):
    B[j,] = list(map(int, input().split()))
   
  print(A+B)
  print(A-B)
  print(A*B)
  print(A//B)
  print(A%B)
  print(A**B)
  CloseIO()