# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./076_np_Transpose_Flatten_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given a NxM integer array matrix with space separated elements 
# (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# In 
# The first line contains the space separated values of N and M
# The next N lines contains the space separated elements of M columns.
# 2 2
# 1 2
# 3 4


# Out 
# [[1 3]
#  [2 4]]
# [1 2 3 4]


if __name__ == '__main__':
  # N lines, M col
  N, M = map(int, input().split())
  my_array = np.empty((N, M), int)

  for j in range(N):
    lst = list(map(int, input().strip().split(' ')))
    my_array[j, ] = lst

  print (my_array.transpose())
  print (my_array.flatten())

  CloseIO()

