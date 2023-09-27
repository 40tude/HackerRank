# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=false

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./046_Symmetric_Difference_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
if __name__ == '__main__':
  m = int(input())
  A = set(map(int, input().split()))
  n = int(input())
  B = set(map(int, input().split()))
  C = A.union(B) - A.intersection(B)
  C = list(C)
  C.sort()
  [print (n) for n in C]  
  CloseIO()
