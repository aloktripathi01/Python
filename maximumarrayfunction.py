def largest(n,array):
	num=max(array)
	return num


array=[]
n=int(input("Enter the length of array:"))
print("Enter the elemnet")

for i in range(0,n):
	b=[]
	b.append(int(input()))
array.append(b)

ans=largest(n,array)
print("Maximum element in array is {}".format(ans))