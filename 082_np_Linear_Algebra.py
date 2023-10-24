
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./082_Linear_Algebra_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a square matrix A with dimensions nxn 
# Your task is to find the determinant. 
# Note: Round the answer to 2 places after the decimal.

# In 
# 2
# 1.1 1.1
# 1.1 1.1

# Out 
# 0.0

if __name__ == '__main__':
  
  n = int(input())
  a = [list(map(float, input().split())) for _ in range(n)]
  #print (f"{np.linalg.det(a):.2f}")  # Affiche 0.00 et 3.14
  print(round(np.linalg.det(a), 2))   # Affiche 0.0 et 3.14

  
  # bob=0.0
  # print (f"{bob:.2f}")  
  # print(round(bob, 2))

  CloseIO()