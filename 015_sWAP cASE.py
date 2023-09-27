import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./015_sWAP cASE_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def swap_case(InStr:str) -> None:
  # OutStr = ""
  # for c in InStr:
  #   if(c.islower()):
  #     OutStr += c.upper()
  #   else:
  #    OutStr += c.lower()
  # return(OutStr)
  print(InStr.swapcase())
  
if __name__ == '__main__':
  swap_case(input())
  CloseIO()
