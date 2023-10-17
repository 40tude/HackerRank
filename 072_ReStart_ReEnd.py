# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./072_ReStart_ReEnd_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given 2 strings k and S
# Your task is to find the indices of the start and end of string k in S


# In 
# aaadaa
# aa

# Out 
# (0, 1)  
# (1, 2)
# (4, 5)

# https://stackoverflow.com/questions/34774126/re-finditer-returning-same-value-for-start-and-end-methods
# removing is not going to work (I want overlap)
# start() and end() return the same value
# I need to add the length by hand
# Je dois sortir -1 si y a rien d'où la "bidouille" avec le if
if __name__ == '__main__':

  S = input().strip()
  k = input().strip()
  S="jjhv"
  k="z"
  
  if re.search(k, S) is not None:
    pattern = f"(?=({k}))"
    matches = re.finditer(pattern, S)
    [print(f"({match.start()}, {match.start()+len(k)-1})") for match in matches]
  else:
    print ("(-1, -1)")

  CloseIO()

  

# re.findall(pattern, string) returns a list of matching strings.
# re.finditer(pattern, string) returns an iterator over MatchObject objects.