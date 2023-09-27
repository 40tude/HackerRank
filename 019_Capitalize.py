# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./019_Capitalize_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def solve1(s):
  return s.title()         # title cannot be used because 12abc when capitalized must remain 12abc.
  # return "12abc".title()

# chris alan
# 1 w 2 r 3g
# 1 2 2 3 4 5 6 7 8  9
def solve2(s):
  answer = ""
  list = s.split()
  for w in list:
    if w[0].isalpha():
      answer +=w.title() + " "
    else :
      answer +=w + " "
  answer = answer.rstrip() # remove the very end space
  return answer

# s consists of alphanumeric characters and spaces.
def solve(s):                # must keep track of spaces => cannot use split
  Answer = ""
  bInWord = False
  for i in range (len(s)):
    if s[i].isspace()!=True and bInWord==False:
      bInWord=True
      Answer += s[i].upper()
    elif s[i].isspace()!=True and bInWord==True:
      Answer += s[i]
    else:
      Answer += s[i]
      bInWord=False
  return Answer    
      


  list = s.split()
  for w in list:
    if w[0].isalpha():
      Answer +=w.title() + " "
    else :
      Answer +=w + " "
  Answer = Answer.rstrip() # remove the very end space
  return Answer



if __name__ == '__main__':
  s = input()
  result = solve(s)
  print(result + '\n')
  CloseIO()