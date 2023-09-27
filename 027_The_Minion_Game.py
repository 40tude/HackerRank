# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./027_The_Minion_Game_Inputs.txt")

def CloseIO() -> None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def GetScore(s, Letters):
  pts = 0
  for i, c in enumerate(s):
    if c in Letters:
      long = len(s)-i
      pts += long
  return pts    

def Minion_Game(s):
  R1 = GetScore(s, "BCDFGHJKLMNPQRSTVWXYZ")
  R2 = GetScore(s, "AEIOU")
  if R1 == R2 :
    print(f"Draw")
  elif R1>R2 :
    print(f"Stuart {R1}")
  else :    
    print(f"Kevin {R2}")
  return 

if __name__ == '__main__':
  s = input()
  Minion_Game(s)
  CloseIO()

# Kevin substring starting with a voyel
# Stuart substring starting with a consonnant
# Print Draw if no winner
# s in uppercase

""""
def Stuart(s):
  Consonnants = "BCDFGHJKLMNPQRSTVWXYZ"
  pts = 0
  for i, c in enumerate(s):
    if c in Consonnants:
      long = len(s)-i
      pts += long
  return pts    

def Kevin(s):
  Voyels = "AEIOU"
  pts = 0
  for i, c in enumerate(s):
    if c in Voyels:
      long = len(s)-i
      pts += long
  return pts
"""

"""
# Kevin substring starting with a voyel
# Stuart substring starting with a consonnant
# Print Draw if no winner
# s in uppercase
def Minion_Game(s):
  R1 = Stuart(s)
  R2 = Kevin(s)
  if R1 == R2 :
    print(f"Draw")
  elif R1>R2 :
    print(f"Stuart {R1}")
  else :    
    print(f"Kevin {R2}")
  return 

if __name__ == '__main__':
  s = input()
  Minion_Game(s)
  CloseIO()
"""

# Comment on fait pour BANANI?

"""
# Pour chaque consonne trouvée
# L'ajouter à une liste
# Pour chaque consonne de la liste
# Compter le nombre de fois que la sous-chaine apparaît dans s
# Ajouter ce nombre au total des points

def Stuart(s):
  Consonnants = "BCDFGHJKLMNPQRSTVWXYZ"
  # Trouver les consonnes de s
  MyList=[]
  for c in Consonnants:
    index = 0
    while index < len(s):
      index = s.find(c, index)
      if index == -1:
        break
      print(f"{c} found at index {index}")
      MyList.append(c)
      index += 1 
"""