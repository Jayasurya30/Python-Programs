a=[[]for _  in range(3)]
b=[[]for _  in range(3)]
c=[[]for _  in range(3)]
print("Enter the elements of the matrix:")
for i in range(3):
    for j in range(3):
        a[i].append(int(input()))
print("Matrix will be:")
for i in range(len(a)):
    print(a[i])
print("Transpose of the matrix will be:")
for i in range(len(b)):
    for j in range(len(b)):
        b[i].append(a[j][i])
for i in range(len(b)):
    print(b[i])
print("Addition of matrix will be:")
for i in range(len(c)):
    for i in range(len(c)):
        c[i].append(0)
for i in range(len(c)):
    for j in range(len(c[0])):
        c[i][j]=a[i][j]+b[i][j]
for i in range(len(c)):
    print(c[i])
  
