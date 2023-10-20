

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./$$TXT_TO_REPLACE$$")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given ...
# Your task is to ...

# In 
# ...

# Out 
# ...

if __name__ == '__main__':
  
  # code
  CloseIO()