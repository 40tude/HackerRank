# V2 voir la boucle do...while et l'opérateur d'assignation
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) # KeepInMind
    arr.sort()
    max = arr.pop()
    while True :
     if (max != (m := arr.pop())):
        break
    print(m)    
        
# V1
# if __name__ == '__main__':
#     n = int(input())
#     # fait la conversion en int. Retourne une map
#     arr = map(int, input().split())
#     arr = list(arr)
#     arr.sort()
#     max = arr.pop()
#     second = arr.pop()
#     while (max == second) :
#         second = arr.pop()
#     print(second) 

    