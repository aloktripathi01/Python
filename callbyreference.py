def swap(*num3,*num4):
	*num3,*num4=*num4,*num3
	print("The value after  swapping is num1={} and num2={}".format(*num3,*num4))
	


num1=int(input("Enter the first no:"))
num2=int(input("Enter the second no :"))
print("The value before swapping is num1={} and num2={}".format(num1,num2))
num3=&num1
num4=&num2
swap(num3,num4)