#program to find gross salary
bs=int(input("Enter basic salary :"))
da=(bs*10)//100
ta=(bs*12)//100
gs=bs+da+ta
print("Gross salary is {}".format(gs))