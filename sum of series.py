num=int(input("Enter the range of series :"))
sum=0
for i in range (1,num+1):
	sum=sum+(1/i)
	print(1/i,end=" +")
	
print("\n sum of series is ={}".format(sum))