num=int(input("enter the no which you want to get factorial :"))
fact=1
for i in range(1,num+1):
	fact=fact*i
print("Factorial of {} is = {}".format(num,fact))