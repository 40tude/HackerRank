# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy as np
import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
    gCwd = os.getcwd()
    gScriptDir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(gScriptDir)
    sys.stdin = open("./077_np_concatenate_Inputs.txt")


def CloseIO() -> None:
    if RedirectIOToFile:
        sys.stdin.close()
        os.chdir(gCwd)


# You are given ...
# Your task is to ...

# In
# You are given two integer arrays of size NxP and M*P
# N & M are rows
# P is the column.
# Your task is to concatenate the arrays along axis 0

# 4 3 2
# 1 2
# 1 2
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4

# Out
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]

# TO DO : see np.loadtxt()
if __name__ == "__main__":
    # N,M lines P col
    N, M, P = map(int, input().split())

    my_list = []
    npa = np.empty((N, P), int)
    for j in range(N):
        my_list = list(map(int, input().split()))
        npa[j,] = my_list

    npb = np.empty((M, P), int)
    for j in range(M):
        my_list = list(map(int, input().split()))
        npb[j,] = my_list

    print(np.concatenate((npa, npb), axis=0))

    CloseIO()
