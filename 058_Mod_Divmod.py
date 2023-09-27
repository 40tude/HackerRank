# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=false
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./058_Mod_Divmod_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 
177
10

# Out 
17
7
(17, 7)

if __name__ == '__main__':
  a = int(input().strip())
  b = int(input().strip())
  print(a//b)
  print(a%b)
  print(divmod(a, b))
  CloseIO()
