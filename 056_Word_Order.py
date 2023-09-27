# https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./056_Word_Order_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Out 
# 3 : number of distinct words from the input.
# 2 1 1 : number of occurrences for each distinct word according to their appearance in the input

# Counter remember the order of insertion

if __name__ == '__main__':
  MyList=[]
  for _ in range(int(input().strip())):
    MyList.append(input().strip()) 
  MyCounter = Counter(MyList)
  print(len(MyCounter))
  [print(MyCounter.get(i), end=' ') for i in MyCounter]
  
  CloseIO()
