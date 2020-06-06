row=int(input("Enter the no of rows of first matrix:"))

col=int(input("Enter the no of coloumn of first matrix:"))

print("Enter the Element of matrix of first matrix:")

# Initialize matrix 1
matrix1 = []
result=[]
# For user input
for i in range(row):  # A for loop for row entries
	a = []
	for j in range(col): # A for loop for column entries
		print("Enter the {}{} element of first matrix :".format(i,j))
		a.append(int(input()))
	matrix1.append(a)
	
row2=int(input("Enter the no of rows of second matrix:"))

col2=int(input("Enter the no of coloumn of second matrix:"))

print("Enter the Element of matrix of second matrix:")

mat = [[int(input()) for x in range (col2)] for y in range(row2)]
for i in range(0,row):
	b=[]
	for j in range(0,col):
		b.append(0)
	result.append(b)

# iterate through rows
for i in range(row):
	# iterate through columns
	for j in range(col):
		result[i][j] = matrix1[i][j] + mat[i][j]

for r in result:
	print(r)
