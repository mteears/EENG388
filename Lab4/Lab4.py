# Lab4
# Matthew Teears

# imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from scipy import stats


def countx(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count


# definitions
Count = []
X_Uniform = []
X_Binomial = []
X_Geometric = []
PMF_X_Uniform = []
PMF_X_Binomial = []
PMF_X_Geometric = []
Uniform_Count = []
Binomial_Count = []
Geometric_Count = []

print("Name: Matthew Teears")
print("Course: EENG388")
print("Lab #03: Binomial Probability Distribution")


for i in range(0, 10):
    Count.append(i+1)

X1 = stats.uniform(0, 10)
X2 = stats.binom(10, 0.9)
X3 = stats.geom(0.5)

for i in range(0, 10):
    X_Uniform.append(X1.rvs())
    X_Binomial.append(X2.rvs())
    X_Geometric.append(X3.rvs())

for i in range(0, 10000):
    PMF_X_Uniform.append(np.math.floor(X1.rvs()))
PMF_X_Uniform.sort()
for i in range(0, 10):
    Uniform_Count.append(countx(PMF_X_Uniform,i)/10000)

# for i in range(0,10000):
#    PMF_X_Binomial.append(np.math.floor(X2.rvs()))
# PMF_X_Binomial.sort()
for i in range(0,10):
    Binomial_Count.append(X2.pmf(i))

# for i in range(0,10000):
#    PMF_X_Geometric.append(np.math.floor(X3.rvs()))
# PMF_X_Geometric.sort()
for i in range(0,10):
    Geometric_Count.append(X3.pmf(i))

print(Geometric_Count)
y_pos = np.arange(len(Count))
fig, axs = plt.subplots(2, 3, figsize=(15, 15))

fig.suptitle('Lab 4. Teears', fontsize=16)

axs[0, 0].plot(Count,X_Uniform)
axs[0, 1].plot(Count,X_Binomial)
axs[0, 2].plot(Count,X_Geometric)
axs[1, 0].bar(y_pos,Uniform_Count)
axs[1, 1].bar(y_pos,Binomial_Count)
axs[1, 2].bar(y_pos,Geometric_Count)

axs[0 ,0].set_title('Raw data X, where X ~ Uniform(0,10)')
axs[0, 1].set_title('Raw data X, where X ~ Binomial(10,0.5)')
axs[0, 2].set_title('Raw data X, where X ~ Geometric(0.5)')
axs[1, 0].set_title('PMF of X, where X ~ Uniform(0,10)')
axs[1, 1].set_title('PMF of X, where X ~ Binomial(10,0.5)')
axs[1, 2].set_title('PMF of X, where X ~ Geometric(0.5)')
#
#
plt.show()



