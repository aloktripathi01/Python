# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:06:46 2020

@author: pravesh
"""

num=int(input("Enter the value of n:"))
num2=float(input("Enter the value of x:"))
y=1
count=1
while count<=num:
    y=y*num2
    count=count+1
    
print("The value of {} and {} power is {}".format(num2,num,y))