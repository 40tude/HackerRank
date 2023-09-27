#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip()) # KeepInMind
    if n%2 != 0 :       # impair
        print("Weird")
    else:                   # pair
        if n>=2 and n <=5 :
            print("Not Weird")
        elif n>=6 and n<=20 :
            print("Weird")
        else :
            print("Not Weird")    
