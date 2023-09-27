# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

import math
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./025_String_Formatting_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# Given an integer, n, print the following values for each integer i from 1 to n :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# Each value should be space-padded to match the width of the binary value of n and the values should be separated by a single space.
#    1    1    1    1
#    2    2    2   10
#    3    3    3   11
#    4    4    4  100
#    5    5    5  101
#    6    6    6  110


if __name__ == '__main__':
  n = int(input( ))
  MaxNbDigits = 1+int(math.log(n)//math.log(2))                 # KeepInMind
  for i in range(1, n+1):
    # https://docs.python.org/3/library/string.html#grammar-token-format-string-conversion
    print(f"{i: >{MaxNbDigits}d}", end=' ')                     
    print(f"{i: >{MaxNbDigits}o}", end=' ')                     # KeepInMind
    print(f"{i: >{MaxNbDigits}X}", end=' ')
    print(f"{i: >{MaxNbDigits}b}", end='\n')
  
  CloseIO()


  