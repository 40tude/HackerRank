# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

import re

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./068_Map_And_Lambda_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# 5

# Out 
# A list on a single line containing the cubes of the first N fibonacci numbers.
# [0, 1, 1, 8, 27]

cube = lambda x: x**3  

def fibonacci(n):
  if (n==0):
    return []
  elif (n==1):
    return [0]
  else :
    l = [0, 1]
    for i in range(2,n):
      l.append(l[i-2]+l[i-1])
    return l  

if __name__ == '__main__':
  n = int(input())
  print(list(map(cube, fibonacci(n))))
  CloseIO()

  