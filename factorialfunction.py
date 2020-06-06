def fact(num):
	ans=1
	for i in range(1,num+1):
		ans=ans*i
	return ans


num=int(input("Enter the number for finding factorial :"))
result=fact(num)
print("The factorial of {} is = {}".format(num,result))