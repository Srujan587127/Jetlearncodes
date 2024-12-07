matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(len(matrix))
print(matrix[2][2])
for i in range(0,len(matrix)):
    for j in range (0,len(matrix[0])):
      print(matrix[i][j], end=" ")
    print("\n")

 
rows = int(input("What is the number of rows?"))
colums = int(input("What is the number of colums?"))

matrix = []
for a in range(rows):
    temp = []
    for b in range(colums):
      x = int(input("Enter your element:"))
      temp.append(x)
    matrix.append(temp)
    print(matrix)
   
for p in range(rows):
    for d in range(colums):
      print(matrix[p][d], end=" ")
    print("\n")


