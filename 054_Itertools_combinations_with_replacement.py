# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./054_Itertools_combinations_with_replacement_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# HACK 2
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
if __name__ == '__main__':
  MyString, k = input().split()
  MyString = "".join(sorted(MyString))
  for i in combinations_with_replacement(MyString, int(k)):
    [print(c, end='') for c in i]
    print()

  CloseIO()
