def table(num):
	for i in range(1,11):
		print("{} X {} is = {}".format(num,i,num*i))
num=int(input("Enter the number for printing table :"))
table(num)