# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

# https://docs.python.org/fr/3.10/library/collections.html
from collections import Counter   

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./030_Collection_Counters_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)
  
if __name__ == '__main__':
  NbShoes = int(input())
  Stock = Counter(list(map(int, input().split())))   # KeepInMind

  NbRequests = int(input())
  Requests=[]
  for i in range(NbRequests):
    #Requests.append(list(map(int, input().split())))
    Requests.append(tuple(map(int, input().split())))

  Total = 0
  for Request in Requests:
    Size = Request[0]
    if Stock[Size]:
      Stock[Size] -=1
      Total += Request[1]
  print(Total)        
  CloseIO()

