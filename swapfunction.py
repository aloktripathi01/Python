def swap(num1,num2):
	num1,num2=num2,num1
	print("The values of num1 is {} and values of num2 is {} after swaping".format(num1,num2))

num1=int(input("Enter first number:"))
num2=int(input("Enter second no:"))
print("The values of num1  is {} and num2 is {} before swapping".format(num1,num2))
swap(num1,num2)