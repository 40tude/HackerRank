# You are given three integers x,y,z
# representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
# Here 0<=i<=x etc. 
# Please use list comprehensions rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    MaList = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) !=n] # KeepInMind
    print(MaList)