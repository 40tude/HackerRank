# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=false

from collections import Counter 

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./061_The_Captain_s_Room_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# Out 
# Output the Captain's room number.
# 8

_ = int(input())
MyCounter = Counter(list(map(int, input().split()))) 
# [print(f"{k}") for k,v in MyCounter.items() if(v==1)] 

tmp = (MyCounter.items())
tmp = sorted(tmp, key = lambda room : room[1], reverse=True)
print(tmp.pop()[0])
CloseIO()

