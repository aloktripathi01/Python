row = int(input("Enter the no of rows of first matrix:"))

col = int(input("Enter the no of coloumn of first matrix:"))

print("Enter the Element of matrix of first matrix:")

# Initialize matrix 1
matrix1 = []
result = []
# For user input
for i in range(row):  # A for loop for row entries
	a = []
	for j in range(col):  # A for loop for column entries
		print("Enter the {}{} element of first matrix :".format(i, j))
		a.append(int(input()))
	matrix1.append(a)
for r in matrix1:
	print(r)
print("Transpose of matrices is :")
for i in range (0,col):
	b=[]
	for j in range(0,row):
		b.append(0)
	result.append(b)
	
for i in range (0,row):
	for j in range(0,col):
		result[j][i]=matrix1[i][j]

for r in result:
	print(r)
		
