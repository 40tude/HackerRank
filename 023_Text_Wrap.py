# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

import sys
import os
import textwrap

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./023_Text_Wrap_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# Insert in String a '\n' every Width char
# AZERT
# AZ\nER\nT
def wrap1(String, Width):
  Para = ""
  i=0
  while i<len(String):
    Para += String[i:i+Width] + "\n"
    i += Width
  return Para

# https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
def wrap(String, Width):
  wrapper = textwrap.TextWrapper(width=Width)
  return(wrapper.fill(text=String))                  # KeepInMind : fill retourne une chaine pas une liste


if __name__ == '__main__':
  string, max_width = input(), int(input())
  result = wrap(string, max_width)
  print(result)
  CloseIO()