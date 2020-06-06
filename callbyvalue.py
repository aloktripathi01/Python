def swap(num1,num2):
	num1,num2=num2,num1
	print("The value of num1={} and num2={} after swaping".format(num1, num2))

num1=int(input("Enter the first no:"))
num2=int(input("Enter the second no :"))
print("The value before swapping is num1={} and num2={}".format(num1,num2))
swap(num1,num2)


