# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./040_Calendar_Module_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  MyDate = list(map(int, input().split()))
  WeekDayId = calendar.weekday(MyDate[2], MyDate[0], MyDate[1])
  print (calendar.day_name[WeekDayId].upper())

  CloseIO()