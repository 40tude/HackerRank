
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./085_np_MeanVarStd_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a 2-D array of size X.
# Your task is to find:
# The mean along axis 1 
# The var along axis 0
# The std along axis none

if __name__ == '__main__':
  
  n, m = map(int, input().split())
  A = np.empty((n, m), dtype=int)  
  for j in range(n):
    A[j,] = list (map(int, input().split()))
  
  print(np.mean(A, axis=1))
  print(np.var(A, axis=0))
  #print(f"{np.std(A):.11f}")
  print(round(np.std(A), 11))
  CloseIO()