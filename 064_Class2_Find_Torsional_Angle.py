# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true
import math

import sys
import os

RedirectIOToFile = True

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./064_Class2_Find_Torsional_Angle_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

# In 
# 0 4 5
# 1 7 6
# 0 5 9
# 1 7 2

# Out 
# 8.19

# AB = B-A

# X = AB x BC cross prod
# Y = BC x CD
# cos(phi) = X.Y/|X||Y| dot prod


class Vect(object):
  def __init__(self, A, B):
    self.x = B.x - A.x
    self.y = B.y - A.y
    self.z = B.z - A.z

  def dot(self, no):
    return self.x * no.x + self.y * no.y + self.z * no.z
  
  def cross(self, other):
    x = self.y * other.z -  self.z * other.y    
    y = self.z * other.x -  self.x * other.z    
    z = self.x * other.y -  self.y * other.x  
    return Vect(Point(0,0,0), Point(x, y, z))          # les 2 extrémités du vecteur

  def ValAbs(self):
    return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

class Point(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

if __name__ == '__main__':

  MyPoints = list()
  for i in range(4):
    pt = list(map(float, input().split()))
    MyPoints.append(pt)

  A, B, C, D = Point(*MyPoints[0]), Point(*MyPoints[1]), Point(*MyPoints[2]), Point(*MyPoints[3])
    
  AB = Vect(A, B)
  BC = Vect(B, C)
  CD = Vect(C, D)

  X = AB.cross(BC)
  Y = BC.cross(CD)

  CosPhi = X.dot(Y)/(X.ValAbs() * Y.ValAbs())
  print(f"{math.degrees(math.acos(CosPhi)):.2f}")

  CloseIO()

  '''
class Points(object):
    def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z

    def __sub__(self, other):
      return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
      return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
      x = self.y * other.z -  self.z * other.y    
      y = self.z * other.x -  self.x * other.z    
      z = self.x * other.y -  self.y * other.x 
      return Points(x, y, z) 
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x1 = b-a
    x2 = c-b
    x3 = x1.cross(x2)
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)

    tmp1 = x.dot(y)
    tmp2 = (x.absolute() * y.absolute())

    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
    CloseIO()
'''

