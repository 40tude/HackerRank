# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./048_Set_Discard_Remove_Pop_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
if __name__ == '__main__':
  _ = int(input().strip())                  # le nb de valeurs
  MySet= set(list(map(int, input().split())))

  for _ in range (int(input().strip())): # le nb d'instructions
    cmd = input().split()                # Z! pop n'a pas d'argument
    match cmd[0]:
      case "pop":
        MySet.pop()
      case "remove":
        MySet.remove(int(cmd[1]))
      case "discard":
        MySet.discard(int(cmd[1]))  
      case other:
        assert(False)

  print (sum(MySet))
  CloseIO()
