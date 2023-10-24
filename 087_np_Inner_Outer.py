
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./087_np_Inner_Outer_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# The first line contains the space separated elements of array A.
# The second line contains the space separated elements of array B.
# First, print the inner product.
# Second, print the outer product.


if __name__ == '__main__':
  A = np.array (list(map(int, input().split())))
  B = np.array (list(map(int, input().split())))
  print(np.inner(A,B))
  print(np.outer(A,B))
  
  CloseIO()