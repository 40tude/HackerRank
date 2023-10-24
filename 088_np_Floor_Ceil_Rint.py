
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./088_np_Floor_Ceil_Rint_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a 1-D array,A . Your task is to print the floor, ceil and rint of all the elements of A.

# A single line of input containing the space separated elements of array .
# On the first line, print the floor of A.
# On the second line, print the ceil of A.
# On the third line, print the rint of A.
if __name__ == '__main__':
  A = np.array (list(map(float, input().split())))
  print(np.floor(A))
  print(np.ceil(A))
  print(np.rint(A))
  CloseIO()