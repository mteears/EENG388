#Lab3
#Matthew Teears

#imports
import matplotlib.pyplot as plt
import random
import numpy as np
import math

#definitions
list = []
pmf = []
heads = 0
tails = 0
P=0.5
q = 1-P
num = 10
nx=0
count = []
print("Name: Matthew Teears")
print("Course: EENG388")
print("Lab #03: Binomial Probability Distribution")

print("\nNumber of flips: ",num)

for i in range(0,int(num)+1):
    flip = random.randint(0,1)
    if(flip == 0):
        list.append('T')
        tails = tails + 1
    else:
        list.append('H')
        heads = heads + 1

for t in list:
    print(t, end =" ") 

print("\nNumber of Heads:  ",heads)

print("\n")
for i in range(0,int(num)+1):
    nx = (math.factorial(num))/(math.factorial(i)*math.factorial(num-i))
    pxk = nx * (P ** i)*(q**(num-i))
    pmf.append(pxk)
    print(i,"   ",pxk) 

for i in range(0,11):
    count.append(i)

print(count)
print(pmf)