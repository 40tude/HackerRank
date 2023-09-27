# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./020_Find_a_string_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You have to print the number of times that the substring occurs in the given string
def count_substring(string, sub_string):
  count = 0
  for i in range (len(string)-len(sub_string)+1):
    if string.find(sub_string, i, i+len(sub_string)) != -1: # trouvé
      count+=1
  return count

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()
  count = count_substring(string, sub_string)
  print(count)
  CloseIO()