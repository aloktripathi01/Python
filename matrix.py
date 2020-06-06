row=int(input("Enter the no of rows:"))

col=int(input("Enter the no of coloumn:"))

print("Enter the Element of matrix :")

# Initialize matrix
matrix = []

# For user input
for i in range(row):  # A for loop for row entries
	a = []
	for j in range(col): # A for loop for column entries
		print("Enter the {}{} element of matrix :".format(i,j))
		a.append(int(input()))
	matrix.append(a)

# For printing the matrix
print("The resultant matrix is :")
for i in range(row):
	for j in range(col):
		print(matrix[i][j], end=" ")
	print()
print("Another method given below:")
#R = int(input("Enter the number of rows:"))
#C = int(input("Enter the number of columns:"))

#print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
#entries = list(map(int, input().split()))

# For printing the matrix
#matrix = np.array(entries).reshape(R, C)
#print(matrix)