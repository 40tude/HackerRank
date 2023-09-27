# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#import cmath
import math

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./035_Triangle_Quest_2_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.
# Using anything related to strings will give a score of 0
# Using more than one for-statement will give a score of 0

for n in range(1,int(input())+1): 
  print((((10**n -1)//9)**2))       # voir le //

CloseIO()


# 5

# 1           1 x 1       10^0
# 121        11 x 11      10^1 + 10^0
# 12321     111 x 111     10^2 + 10^1 + 10^0
# 1234321
# 123454321

# Fonctionne mais pas valable car plrs lignes etc.
# m=0
# for n in range(1,int(input())+1): 
#   m=m+10**(n-1)
#   print(m*m) 

# Triangle de Pascal
# [print(round(math.factorial(n)/(math.factorial(p) * math.factorial(n-p))), end='') for p in range(n+1)]; print()

# Pas valide, on a droit qu'à une boucle for
# [print(p, end='') for p in range(1, n+1)]; [print(p, end='') for p in range(n-1, 0, -1)]; print()








