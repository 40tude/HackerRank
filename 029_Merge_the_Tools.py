# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./029_Merge_the_Tools_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def merge_the_tools(s:str, k:int) -> None :
  # build the list of words
  List = [s[i:i+k] for i in range(0, len(s), k)] 

  # remove any subsequent duplicated letter and print the word
  for w in List:        
    Filtered=[]
    for c in w :
      if c not in Filtered:
        Filtered.append(c)
    [print(c, end='') for c in Filtered]  # KeepInMind : print a list
    print()
  
if __name__ == '__main__':
  string, k = input(), int(input())
  merge_the_tools(string, k)
  CloseIO()

