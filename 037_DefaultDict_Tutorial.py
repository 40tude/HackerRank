# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./037_DefaultDict_Tutoarial_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

def def_value():
    return -1

if __name__ == '__main__':
    A_Size, B_Size = map(int, input().split())

    A = []
    B = []
    [A.append(input()) for n in range(A_Size)]
    [B.append(input()) for n in range(B_Size)]

    d = defaultdict(list)                     # default_factory = list - a defaultdict is created with the values that are list.
    # https://stackoverflow.com/questions/5900578/collections-defaultdict-difference-with-normal-dict
    # d.default_factory = lambda : [-1]
    for i, c in enumerate(A):
      d[c].append(i+1)

    for c in B :
      print (-1 if d[c]==[] else ", ".join((map(str,d[c]))))

    CloseIO()



    # d = defaultdict(def_value)
    # for i, c in enumerate(A):
    #   d[c].append(i+1)

    # for c in B :
    #   print (d[c])




    # d = defaultdict(lambda: "Not Present")
    # d["a"] = 1
    # d["b"] = 2
      
    # print(d["a"])
    # print(d["b"])
    # print(d["c"])

    # d = defaultdict(lambda: -1)
    # d["a"] = 1
    # d["b"] = 2
      
    # print(d["a"])
    # print(d["b"])
    # print(d["c"])



    # d = defaultdict(def_value)
    # d["a"] = 1
    # d["b"] = 2
      
    # print(d["a"])
    # print(d["b"])
    # print(d["c"])



    # d = defaultdict(list)                     # default_factory = list - a defaultdict is created with the values that are list.
    # # https://stackoverflow.com/questions/5900578/collections-defaultdict-difference-with-normal-dict
    # # d.default_factory = lambda : [-1]
    # for i, c in enumerate(A):
    #   d[c].append(i+1)

    # for c in B :
    #   print (-1 if d[c]==[] else ", ".join((map(str,d[c]))))
    #   # value_if_true if condition else value_if_false

