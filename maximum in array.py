print("value separated by enter  keyword")
n=int(input("Enter the range of array :"))

arr=[float(input()) for i in range(0,n)]

max=arr[0]
for i in range(0,n):
	if max < arr[i]:
		max=arr[i]
	else:
		continue
print("The maximum no is {}".format(max))