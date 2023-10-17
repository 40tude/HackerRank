# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./071_Refindall_Refinditer_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a string S. 
# It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.

# In 
# rabcdeefgyYhFjkIoomnpOeorteeeeet

# Out 
# ee
# Ioo
# Oeo
# eeeee

if __name__ == '__main__':

  # le truc c'est le bloc de capture dans le lookahead qui permet d'avoir des overlapping matches 
  # gérer le cas qsdqsdaaaabaaaabaaaabdfgdfgdfg
  str = input().strip()
  matches = re.findall(r"(?=([^aeiouAEIOU]{1}([aeiouAEIOU][aeiouAEIOU]+)[^aeiouAEIOU]{1}))", str)
  if len(matches):
    [print(match[1]) for match in matches]
  else:
    print (-1)
  CloseIO()

  