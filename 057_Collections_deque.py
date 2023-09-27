# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./057_Collections_deque_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 


# Out 
if __name__ == '__main__':
  d = deque()
  for _ in range(int(input().strip())):
    instruction = []
    instruction = input().split()
    match(instruction[0]):
      case "append":
        d.append(int(instruction[1]))
      case "appendleft":
        d.appendleft(int(instruction[1]))
      case "pop":
        d.pop()
      case "popleft":
        d.popleft()
      case other:
        assert(False)
  print(*d)
  CloseIO()
