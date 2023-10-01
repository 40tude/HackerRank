# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./067_Detect_Floating_Point_Number_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# Number can start with +, - or . symbol.
# Number must contain at least decimal value.
# Number must have exactly one . symbol.
# Number must not give any exceptions when converted using float(N)
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff

# Out 
# False
# True
# True
# False


if __name__ == '__main__':

  n = int(input().strip())
  
  # Voir aussi https://stackoverflow.com/questions/12643009/regular-expression-for-floating-point-numbers
  # MAIS ça marche pas
  
  MyRegex = r"^[+-]?[0-9]*[.][0-9]*$"
  for i in range(n):
    data = input().strip()
    print (bool(re.match(MyRegex,data)))
  CloseIO()

  