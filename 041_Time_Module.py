# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#import time
from datetime import datetime

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./041_Time_Module_2_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# https://www.programiz.com/python-programming/datetime/strptime
def time_delta(end_time, start_time) :
  # Sun 10 May 2015 13:54:36 -0700
  t1 = datetime.strptime(end_time, "%a %d %b %Y %H:%M:%S %z")
  #print('Start time:', t1.time())
  t2 = datetime.strptime(start_time, "%a %d %b %Y %H:%M:%S %z")
  delta = t1-t2
  return (str(abs(int(delta.total_seconds()))))

if __name__ == '__main__':
  n = int(input())
  for _ in range(n):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    #print(f"{:.0f}")
    print(delta)
  
  CloseIO()
