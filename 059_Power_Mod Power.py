# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=false
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./059_Power_Mod Power_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 
3
4
5

# Out 
81
1

if __name__ == '__main__':
  a = int(input().strip())
  b = int(input().strip())
  m = int(input().strip())
  print(a**b)
  print(pow(a,b,m))
  CloseIO()
