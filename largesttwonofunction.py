def largest(num1,num2):
	if num1 > num2:
		return num1
	else:
		return num2


num1=int(input("Enter the first no:"))
num2=int(input("Enter the second no :"))
ans=largest(num1,num2)
print("The largest no between {} and {} is = {}".format(num1,num2,ans))