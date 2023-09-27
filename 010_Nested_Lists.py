# https://www.hackerrank.com/challenges/nested-list/problem

# Given the names and grades for each student in a class of students, 
# store them in a nested list 
# and print the name(s) of any student(s) having the second lowest grade.
# If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

# Je pense que j'ai pas compris l'interret
# J'aurai fait un tableau d'objets student ou un tableau de tuples

if __name__ == '__main__':
  Students=[]
  for _ in range(int(input())):                                    # KeepInMind
    name = input()
    score = float(input())
    Students.append([name, score])
  # classe par ordre alpha decroissant et par notes decroissantes
  Students.sort(key=lambda student : student[0], reverse = True)   # KeepInMind
  Students.sort(key=lambda student : student[1], reverse = True)
  
  Worst = Students.pop()
  # On cherche la 2eme plus mauvaise note
  while (Current := Students.pop()):                               # KeepInMind
    if Current[1]>Worst[1]:
      print(Current[0])
      break

  n = len(Students)
  Score = Current[1] 
  # Affiche les noms si même note
  for i in range(n):
    Current = Students.pop()
    if(Current[1]!=Score):
      break
    print(Current[0])
