import numpy as np
num1=int(input("Enter the elements size of first array:"))
print("Enter the elements:")
lst1=[]
for i in range(0, num1):
	ele = int(input())
	
	lst1.append(ele)
	
num2=int(input("Enter the element size of second array:"))
print("Enter the elements:")
lst2=[]
for i in range(0, num2):
	ele = int(input())
	
	lst2.append(ele)

lst3=lst1+lst2
print(lst3)
			
b = set()
unique = []
for x in lst3:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)
