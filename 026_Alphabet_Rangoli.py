# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./026_Alphabet_Rangoli_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(n):
  # Answer=""

  Width = (2*n)-1 + 2*(n-1)
  Alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
  Fill  = "- - - - - - - - - - - - - - - - - - - - - - - - - -".split()
  Merge = Alpha + Fill        # KeepInMind : mixt of 2 list
  Merge[::2] = Alpha
  Merge[1::2] = Fill

  Stack = []
  for i in range(1, n+1):
    Rhs = Merge[2*(n-i):2*n-1]
    Lhs = Rhs[::-1]
    Lhs.pop()
    Line = "".join(Lhs+Rhs)
    print(f"{Line:-^{Width}}")
    #Answer +=f"{Line:-^{Width}}" + "\n"
    Stack.append(Line)
  
  Stack.pop()
  for l in Stack[::-1]:
    print(f"{l:-^{Width}}")
    #Answer +=f"{l:-^{Width}}" + "\n"
  # return Answer  

if __name__ == '__main__':
  n = int(input())
  print_rangoli(n)
  CloseIO()