#program to reverse a no
n=int(input("Enter the no: "))

rev = 0

while (n > 0):
    a= n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)


