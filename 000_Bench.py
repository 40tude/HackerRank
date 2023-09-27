# import timeit
# s = """\
# Alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
# Fill  = "- - - - - - - - - - - - - - - - - - - - - - - - - -".split()
# Merge = Alpha + Fill
# Merge[::2] = Alpha
# Merge[1::2] = Fill  # Merge est une liste
# """
# # CTRL + F5 => Sans debug
# print(timeit.timeit(stmt=s, number=100000))





################################################################################
# 0.0009 sans debug
import time
from collections import Counter 

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

def EvalHappiness (A, B, MyList): 
  Happiness = 0
  for k, v in MyList.items():
    if k in A:
      Happiness += v
    elif k in B:                         
      Happiness -= v
  return Happiness

if __name__ == '__main__':
  n, m = map(int, input().split())
  c = Counter(list(map(int, input().split()))) 
  MyList = dict(c) 
  A = Counter(map(int, input().split()))
  B = Counter(map(int, input().split()))
  
  start_time = time.perf_counter()
  Happiness = EvalHappiness(A, B, MyList)
  end_time = time.perf_counter()
  total_time = end_time - start_time
  print(f'Total execution time: {total_time} seconds')
  
  print(f"{Happiness}")    
  CloseIO()
################################################################################

################################################################################
# 0.009 sans debug
# import time
# from collections import Counter 

# import sys
# import os

# RedirectIOToFile = True

# if RedirectIOToFile:
#   gCwd = os.getcwd()
#   gScriptDir = os.path.dirname(os.path.realpath(__file__))
#   os.chdir(gScriptDir)
#   sys.stdin = open("./045_No_Idea_2_Inputs.txt")

# def CloseIO()->None:
#   if RedirectIOToFile:
#     sys.stdin.close()
#     os.chdir(gCwd)

# if __name__ == '__main__':
#   n, m = map(int, input().split())
#   c = Counter(list(map(int, input().split()))) 
#   start_time = time.perf_counter()
#   MyList = dict(c) 
#   A = tuple(map(int, input().split()))
#   B = tuple(map(int, input().split()))
#   Happiness = 0
#   for k, v in MyList.items():
#     if k in A:
#       Happiness += v
#     elif k in B:                         
#       Happiness -= v
#   end_time = time.perf_counter()
#   total_time = end_time - start_time
#   print(f'Total execution time: {total_time} seconds')
#   print(f"{Happiness}")    
#   CloseIO()
################################################################################







