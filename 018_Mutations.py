import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./018_Mutations_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def mutate_string(string, i, c):
  return string[:i] + c + string[i+1:] # KeepInMind : slicing & joining - insère c à l'indice i

if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)
  CloseIO()