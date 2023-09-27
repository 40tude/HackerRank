# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./055_Compress_The_String_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)
# In = 1222311
# Out = 1, 1) (3, 2) (1, 3) (2, 1)
if __name__ == '__main__':
  MyString = input().strip()


  # Groups = []
  # Uniquekeys = []
  #MyString = sorted(MyString)
  for k, g in groupby(MyString):
    #tmp = list(g)
    #Groups.append(tmp)      
    #Uniquekeys.append(k)
    # le # de valeurs, la valeurs en question
    print(f"({len(list(g))}, {k})", end=' ')
    # MyDict[k] = len(list(g))

  # print()
  # print(Groups)
  # print(Uniquekeys)
  # print(MyDict)

  CloseIO()
