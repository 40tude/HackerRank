# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=false

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./047_Set_Add_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# Find the total number of distinct country stamps.
if __name__ == '__main__':
  MySet=set()
  for _ in range (int(input().strip())):
    MySet.add(input())
  print (len(MySet))
  CloseIO()
