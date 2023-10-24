
import re
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./089_Validate_Phone_Num_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# A valid mobile number is a 
# ten digit number 
# starting with 7 a 8 or 9.

# In 
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.

# Out 
# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

if __name__ == '__main__':

  n = int(input().strip())
  pattern = r"^[789]\d{9}$"
  for i in range(n):
    Phone = input().strip()
    print("YES") if re.match(pattern, Phone) else print("NO")
  CloseIO()