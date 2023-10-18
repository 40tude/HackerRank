# https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true

import re
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./073_Validating-Roman_Numerals_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a string, and you have to validate whether it's a valid Roman numeral. 
# If it is valid, print True. 
# Otherwise, print False. 
# Try to create a regular expression for a valid Roman numeral.
# The number will be between 1 and 3999 (both included)

# In 
# CDXXI

# Out 
# True

# Notes
# https://vitrinelinguistique.oqlf.gouv.qc.ca/24335/la-typographie/nombres/ecriture-des-chiffres-romains
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 et M = 1000.
# Sauf pour I (et M) 3 instances max
# Pour I et M 4 instances max
# Ici on limite à 3 même pour I et M

# https://developers.google.com/edu/python/regular-expressions?hl=fr

if __name__ == '__main__':

  roman = input().strip()
  if re.match(r"[IVXLCDM]+", roman):
    print("True")
  else:
    print("False")  

  # print(str(bool(re.match(regex_pattern, input()))))
  CloseIO()
  
