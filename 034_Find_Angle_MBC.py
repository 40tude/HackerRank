# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#import cmath
import math

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./034_Find_Angle_MBC_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  y = float(input())
  x = float(input())

  alpha = round(math.degrees(math.atan(y/x)))
  #tmp = "°".encode("utf-8")
  print (f"{alpha}\xb0")  
  CloseIO()

# The first line contains the length of side AB (vertical)
# The second line contains the length of side BC (hori)
# Round the angle to the nearest integer.
# Output the angle in degrees .