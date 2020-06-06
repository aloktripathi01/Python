# program to find greatest of three no
a,b,c=[int(x) for x in input("Enter the three value  :").split()]

if a>b:
	if b>c:
		print("a is gretest {}".format(a))

if b>a:
	if b>c:
		print("b is gretest {}".format(b))

if c>b:
	if c>a:
		print("c is gretest {}".format(c))
