# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./024_Designer_Door_Mat_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

if __name__ == '__main__':
  Height, Width = map(int, input( ).split())
  
  Pattern = ".|."
  
  for i in range(1, Height, 2):
    print(f"{Pattern*i:-^{Width}}")           # KeepInMind
  
  print(f"{'WELCOME':-^{Width}}")
  
  for i in range(Height-2, 0, -2):
    print(f"{Pattern*i:-^{Width}}")
 
  CloseIO()