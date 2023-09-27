# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=false
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./060_Integers_Come_In_All_Sizes_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)


# In 
# 9
# 29
# 7
# 27

# Out 
# Print the result of a^b + c^d on one line.
# 4710194409608608369201743232  

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b+c**d)

CloseIO()

