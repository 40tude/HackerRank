# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=false

from collections import Counter 
import timeit

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./045_No_Idea_2_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# Utiliser des dictionnaires
if __name__ == '__main__':
  n, m = map(int, input().split())
  c = Counter(list(map(int, input().split()))) 
  MyList = dict(c) 
  A = Counter(map(int, input().split()))
  B = Counter(map(int, input().split()))
  Happiness = 0
  for k, v in MyList.items():
    if k in A:
      Happiness += v
    elif k in B:                         
      Happiness -= v
  print(f"{Happiness}")    
  CloseIO()



# Toujours trop lent
# Regrouper les valeurs dans la liste. Si il y a 5 fois 32
# À la clé 32 on met 5
# if __name__ == '__main__':
#   n, m = map(int, input().split())
#   c = Counter(list(map(int, input().split()))) 
#   MyList = dict(c) 
#   A = tuple(map(int, input().split()))
#   B = tuple(map(int, input().split()))
#   Happiness = 0
#   for k, v in MyList.items():
#     if k in A:
#       Happiness += v
#     elif k in B:                         
#       Happiness -= v
#   print(f"{Happiness}")    
#   CloseIO()


# Too slow approach 2
# Correct however
# if __name__ == '__main__':
#   n, m = map(int, input().split())
#   MyList = tuple(map(int, input().split()))
#   A = tuple(map(int, input().split()))
#   B = tuple(map(int, input().split()))

#   Happiness=0
#   for n in MyList:
#     if n in A:
#       Happiness+=1
#     if n in B:
#       Happiness-=1
#   print(f"{Happiness}")    
#   CloseIO()


# Too slow approach 1
# Y a un bug car si un nb est plusireurs fois dans MyList on ne le compte q'une fois
# if __name__ == '__main__':
#   n, m = map(int, input().split())
#   MyList = tuple(map(int, input().split()))
#   A = tuple(map(int, input().split()))
#   B = tuple(map(int, input().split()))

#   Happiness=0
#   for n in A:
#     if n in MyList:
#       Happiness += 1
#   for n in B:
#     if n in MyList:
#       Happiness -= 1
#   print(f"{Happiness}")    
#   CloseIO()
