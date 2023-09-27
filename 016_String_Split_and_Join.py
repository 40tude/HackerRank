import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./016_String_Split_and_Join_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line) # KeepInMind
    return line

if __name__ == '__main__':
  line = input()
  result = split_and_join(line)
  print(result)
  CloseIO()