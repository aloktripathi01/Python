print("fibonaci sequence up to 100:")

a=0
b=1
print(a,b )
for i in range (1,100):
	c=a+b
	if c>100:
		break
	
	
	else:
		print(c ,end=" ")
		a=b
		b=c
		
	