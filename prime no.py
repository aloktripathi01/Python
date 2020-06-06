num =int(input("Enter the no for checking prime :"))
count=0
for i in range (2,num):
	if num%i==0:
		count=1
		break
	else:
		count=0
		break
if count==0:
	print("{} is prime no".format(num))
else:
	print("{} is not prime no".format(num))