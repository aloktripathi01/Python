str=input("Enter the string for checking Palindrome :")
ans=str[::-1]
if ans==str:
	print("String is palindrome")
else:
	print("String is not palindrome")