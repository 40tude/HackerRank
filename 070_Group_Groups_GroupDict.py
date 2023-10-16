# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import re
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./070_Group_Groups_GroupDict_Inputs.txt")


def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
# In 
# ..12345678910111213141516171820212223

# Out 
# 1

if __name__ == '__main__':
  
  # m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
  # print(m.group(0))
  # print(m.group(1))
  
  # regex_pattern = "(\W+)" 
  # m = re.split(regex_pattern, 'Words, words, words.')
  # print (m)
  # print(m[0])

  str = input().strip()
  m = re.search(r"([a-zA-Z1-9])\1{1,}", str)  # \1 fait réference au 1 groupe
                                              # {1,} une fois de plus (donc 2 fois au minimum) sans limite max

  if(m==None):
    print(-1)
  else:
    #print(m.lastindex)
    print (m[1])
    

  CloseIO()

  