# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./021_String_Validators_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  s = input().strip()
  # In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
  # In the second line, print True if s has any alphabetical characters. Otherwise, print False.
  # In the third line, print True if s has any digits. Otherwise, print False.
  # In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
  # In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
  print("True") if any(letter.isalnum() for letter in s) else print("False")                  # KeepInMind
  print("True") if any(letter.isalpha() for letter in s) else print("False")
  print("True") if any(letter.isdigit() for letter in s) else print("False")
  print("True") if any(letter.islower() for letter in s) else print("False")
  print("True") if any(letter.isupper() for letter in s) else print("False")
  CloseIO()