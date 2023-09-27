# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from statistics import mean

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./042_Zipped_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# 5 3 - students x subjects
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

# out
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5   

if __name__ == '__main__':
  # NbStudents, NbSubjects  = input().split()
  # NbStudents = int(NbStudents)
  # NbSubjects = int(NbSubjects)
  
  NbStudents, NbSubjects = map(int, input().split())
  Results=[]
  for _ in range(NbSubjects):
    Subject = list(map(float, input().split()))
    Results+=[Subject]
  ScoreByStudent = list(zip(*Results))
  [print(f"{mean(ScoreByStudent[i]):.1f}") for i in range(NbStudents)]
  
  CloseIO()
