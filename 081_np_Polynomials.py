
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./081_Polynomials_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given the coefficients of a polynomial P
# Your task is to find the value of P at point x

# In 
# The first line contains the space separated value of the coefficients in P
# The second line contains the value of x
# 1.1 2 3
# 0

# Out 
# 3.0

if __name__ == '__main__':
  
  MyCoef = list(map(float, input().split()))
  x = float(input())
  print(np.polyval(np.array(MyCoef), x))
  CloseIO()