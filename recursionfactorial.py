def fact(num):
	if num == 0:
		return 1
	else:
		return num*fact(num-1)
num=int(input("Enter the number :"))
ans=fact(num)
print("The factorial of {} is = {}".format(num,ans))