import cmath

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./033_Polar_Coordinates_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  cplx = input().strip()
    
  # cplx string cannot have space
  Polar = (cmath.polar(complex(cplx)))
  [print(v)  for v in Polar] 
  CloseIO()

# You are given a complex z. Your task is to convert it to polar coordinates.
# 1+2j
# 2.23606797749979 
# 1.1071487177940904