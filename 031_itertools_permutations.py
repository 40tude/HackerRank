from itertools import permutations

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./031_itertools_permutations_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  Word, k = input().split()
  
  # Enlever les duplicates 
  # Trier les lettres restantes
  Word = list(dict.fromkeys(Word))
  Word.sort()
  Word = "".join(Word) 
  ListOfTuples = list(permutations(Word, int(k)))
  [print("".join(t)) for t in ListOfTuples]
  
  CloseIO()

# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
# HACK 2
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
