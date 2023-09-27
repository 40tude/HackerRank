#!/bin/python3
# You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). 
# You are required to sort the data based on the th attribute and print the final resulting table. 

# Input
# 5 3
# 10 2  5
# 7  1  0
# 9  9  9
# 1  23 12
# 6  5  9
# 1

#Output
# 7  1  0
# 10 2  5
# 6  5  9
# 9  9  9
# 1  23 12

import math
import random
import re
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./Athlete_Sort_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  nm = input().split()
  NbAthletes = int(nm[0])
  NbAttributes = int(nm[1])

  arr = []
  for _ in range(NbAthletes):
    arr.append(list(map(int, input().rstrip().split())))

  AttributeIndex = int(input())

  arr.sort(key=lambda athlete : athlete[AttributeIndex])
  
  # for j in range(NbAthletes) :
  #   for i in range(NbAttributes) :
  #     print(arr[j][i], end=' ')
  #   print()  
  
  for athlete in arr:
    for caract in athlete :
      print(caract, end=' ')
    print()
  
  CloseIO()