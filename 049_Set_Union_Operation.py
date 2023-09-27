# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./049_Set_Union_Operation_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  _ = int(input().strip())                  
  EnglishSet= set(list(map(int, input().split())))
  _ = int(input().strip())                  
  FrenchSet= set(list(map(int, input().split())))
  print (len(EnglishSet.union(FrenchSet)))
  CloseIO()
