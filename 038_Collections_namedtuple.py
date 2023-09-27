# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from collections import namedtuple

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./038_Collections_namedtuple_2_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6   

if __name__ == '__main__':
  N = int(input())

  Col1, Col2, Col3, Col4 = input().split()
  Students = namedtuple('Student',[Col1, Col2, Col3, Col4])

  Class = []
  for i in range(N):
    Col1, Col2, Col3, Col4 = input().split()
    Class.append(Students(Col1, Col2, Col3, Col4))

  Moy = 0.0
  for s in Class:
    Moy+=int(s.MARKS)     
  
  print(f"{Moy/N:.2f}")

  CloseIO()

