# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./066_Any_Or_All_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
# 5
# 12 9 61 5 14 

# Out 
#True

def IsPalindromic(n):
  temp = n
  rev = 0
  while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
  if(temp==rev):
    return(True)
  else:
    return(False)

if __name__ == '__main__':

  _ = input()
  MyList = list(map(int, input().split()))
  print ("True") if all(t > 0 for t in MyList) & any(IsPalindromic(t) for t in MyList) else print("False")
  CloseIO()

  