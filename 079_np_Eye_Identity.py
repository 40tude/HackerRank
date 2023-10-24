import numpy as np

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./079_Eye_Identity_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# Your task is to print an array of size NxM with its main diagonal elements as 's and 's everywhere else.
# Your task is to ...

# In 
# 3 3

# Out 
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

if __name__ == '__main__':
  
  n, m = map(int, input().split())
  #print(np.eye(n, m, n-m))
  print(np.eye(n, m))
  CloseIO()