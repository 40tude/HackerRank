from itertools import combinations

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./032_itertools_combinations_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  Word, k = input().split()
  
  # Trier la chaine dans l'ordre alpha
  Word = "".join(sorted(Word))
  for i in range(1, int(k)+1):
    ListOfTuples = list(combinations(Word, i))
    [print("".join(t)) for t in ListOfTuples]
  
  CloseIO()

# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
# HACK 2
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK