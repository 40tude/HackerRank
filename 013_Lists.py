
# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./013_Lists_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  N = int(input())
  Program = []
  for _ in range(N):
    Instruction = input().split()
    Program.append(Instruction)

  # insert i e: Insert integer e at position i
  # print: Print the list.
  # remove e: Delete the first occurrence of integer .
  # append e: Insert integer  at the end of the list.
  # sort: Sort the list.
  # pop: Pop the last element from the list.
  # reverse: Reverse the list.
  MyList = []
  for Instruction in Program:
    match Instruction[0]:                  # KeepInMind : switch case
      case "insert" :
        MyList.insert(int(Instruction[1]), int(Instruction[2]))
      case "print":
        print(MyList)
      case "remove" :
        MyList.remove(int(Instruction[1]))
      case "append" :
        MyList.append(int(Instruction[1]))
      case "sort" :
        MyList.sort()
      case "pop" :
        MyList.pop()
      case "reverse" :
        MyList.reverse()
      case other :
        assert False  

  CloseIO()