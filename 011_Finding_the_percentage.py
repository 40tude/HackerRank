from statistics import mean

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./Finding_the_percentage_Inputs_2.txt.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  n = int(input())

  student_marks = {}                    # KeepInMind : la façon de créer le dico
  for _ in range(n):
    # *line : the unpacking operator voir https://geekflare.com/python-unpacking-operators/
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
  query_name = input()
  print(f"{mean(student_marks[query_name]):.2f}")

  CloseIO()