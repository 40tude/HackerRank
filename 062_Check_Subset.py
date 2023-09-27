# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./062_Check_Subset_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Out 
# True 
# False
# False

T = int(input().strip())
for i in range(T):
  _ = int(input().strip())
  A = set(map(int, input().split()))
  
  _ = int(input().strip())
  B = set(map(int, input().split()))
  print("True") if A == A.intersection(B) else print("False")

CloseIO()

