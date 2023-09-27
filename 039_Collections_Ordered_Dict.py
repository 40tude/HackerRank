# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import OrderedDict
import re

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./039_Collections_Ordered_Dict_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30 

# Print the item_name and net_price in order of its first occurrence.
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

if __name__ == '__main__':
  n = int(input())
  od = OrderedDict()  
  for i in range (n):
    str = input()
    Val = [int(s) for s in str.split() if s.isdigit()]
    Pdt = [s for s in str.split() if s.isalpha()]
    Pdt = " ".join(Pdt)
    CurrentVal = od.get(Pdt)
    if CurrentVal:
      od[Pdt] += int(Val[0])
    else:
      od[Pdt]  = int(Val[0])

  for key, value in od.items():
    print(key, value)

  # CloseIO()  


  

  

