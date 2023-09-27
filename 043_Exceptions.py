# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./043_Exceptions_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


if __name__ == '__main__':
  n = int(input())
  for _ in range(n):
    try:
      a, b = map(int, input().split())
      r = a//b
    except ValueError as e:
      print (f"Error Code: {e}")
    except ZeroDivisionError as e:
      print (f"Error Code: {e}")
    else:
      # se déroule si pas d'exception  
      print(f"{r}") 
    # finally:
    #   print(f"Whatever happens")   

  CloseIO()
