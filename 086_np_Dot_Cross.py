
import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./086_np_Dot_Cross_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# You are given two arrays A and B. Both have dimensions of n x n.
# Your task is to compute their matrix product.


if __name__ == '__main__':
  
  n = int(input())
  A = np.empty((n, n), dtype=int)  
  B = np.empty((n, n), dtype=int)  
  for j in range(n):
    A[j,] = list (map(int, input().split()))
  for j in range(n):
    B[j,] = list(map(int, input().split()))
  
  # print(np.cross(A,B))
  print(np.dot(A,B))
  
  CloseIO()