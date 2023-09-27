# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./063_Check_Strict_Superset_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# Out 
# False
  
# A strict superset has at least one element that does not exist in its subset.  
A = set(map(int, input().split()))
n = int(input().strip())

bStrict = True
for i in range(n):
  B = set(map(int, input().split()))
  if (len(A.intersection(B))) != len(B) :
    bStrict = False
    break
print(bStrict)  

CloseIO()

