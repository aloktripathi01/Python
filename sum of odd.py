num=int(input("Enter the range of seires :"))
sum=0
for i in range (1,num+1):
	if i%2==0:
		continue
	else:
		sum=sum+i
		print(i,end="+")
print("\n The sum of series is {}".format(sum))