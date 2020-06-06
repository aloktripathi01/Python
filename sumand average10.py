print("Enter the no: ")
sum=0
n=int(input())
arr = [float(input()) for i in range(0,n)]
for i in range(0,n):
	sum=sum+arr[i]
	
print("Sum of array elements is {} and average is {}".format(sum,sum/n))