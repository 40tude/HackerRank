# https://www.hackerrank.com/challenges/py-set-mutations/problem
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./053_Set_Mutations_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

if __name__ == '__main__':
  _ = int(input().strip())                   # Nb element, pas utilisé     
  A = set(list(map(int, input().split())))
  for n in range(int(input().strip())):      # Nb opps à faire
    order, _ = input().split()               # order & nb element du set B
    B = set(list(map(int, input().split())))
    match order:
      case "intersection_update":
        A.intersection_update(B)
      case "update":
        A.update(B)
      case "symmetric_difference_update":
        A.symmetric_difference_update(B)
      case "difference_update":
        A.difference_update(B)
      case other:
        assert(False)
    
  print (sum(A))
  CloseIO()
