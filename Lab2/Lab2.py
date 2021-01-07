#Lab2
#Matthew Teears

#imports
import matplotlib.pyplot as plt
import random
import numpy as np

#definitions
list = []
heads = 0
tails = 0
num = input("How many times to toss the coin? ")
heads = 0
tails = 0


print(num)
for i in range(0,int(num)):
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
print("Number of Tails:  ",tails)

rf_heads = heads/int(num)
rf_tails = tails/int(num)

print("\nRelative Freq. of Heads:  ",rf_heads)
print("Relative Freq. of Tails:  ",rf_tails)  

lab = ['Heads', 'Tails']
count = [heads, tails]
y_pos = np.arange(len(lab))

plt.bar(y_pos, count, align='center', alpha=0.5)
plt.xticks(y_pos, lab)
plt.ylabel('Count')
plt.title('Relative Frequency of Coin Toss')

plt.show()
