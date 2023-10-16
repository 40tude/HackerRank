# https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true

import re

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./069_ReSplit_Inputs.txt")


def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# 100,000,000.000

# Out 
# 100
# 000
# 000
# 000

regex_pattern = r"[,.]"	# Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))