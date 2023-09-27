# https://www.hackerrank.com/challenges/incorrect-regex/problem
import re

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./044_Incorrect_Regex_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  n = int(input())
  for _ in range(n):
    str = input()
    try:
      re.compile(str)
    except re.error:
      print (f"False")
    else:
      print (f"True")

  CloseIO()
