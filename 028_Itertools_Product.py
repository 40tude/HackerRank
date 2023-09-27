# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./028_Itertools_Product_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  #print(list(product(A,B)))
  [print(pt, end=' ') for pt in product(A,B)]       # KeepInMind : on veut pas de "," entre les (x,y)
  CloseIO()

