# Lab4
# Matthew Teears

# imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from scipy import stats

# definitions
nobs = 10000
Count = []
X_Uniform_Raw = []
X_Binomial_Raw = []
X_Geometric_Raw = []
PMF_X_Uniform = []
PMF_X_Binomial = []
PMF_X_Geometric = []
Uniform_Sorted = []
Binomial_Sorted = []
Geometric_Sorted = []

def countx(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count

print("Name: Matthew Teears")
print("Course: EENG388")
print("Lab #05: Binomial Probability Distribution")

X1 = stats.uniform(0, 10)
X2 = stats.binom(10, 0.5)
X3 = stats.geom(0.5)

for i in range(0, nobs):
    Count.append(i + 1)
    X_Uniform_Raw.append(X1.rvs())
    X_Binomial_Raw.append(X2.rvs())
    X_Geometric_Raw.append(X3.rvs())

Uniform_Sorted = np.sort(X_Uniform_Raw)
Binomial_Sorted = np.sort(X_Binomial_Raw)
Geometric_Sorted = np.sort(X_Geometric_Raw)

p1 = np.arange(len(X_Uniform_Raw))/(len(X_Uniform_Raw) - 1)
p2 = np.arange(len(X_Binomial_Raw))/(len(X_Binomial_Raw) - 1)
p3 = np.arange(len(X_Geometric_Raw))/(len(X_Geometric_Raw) - 1)


fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, figsize=(15, 15))
fig.suptitle('Lab 5. Teears', fontsize=16)

ax1.plot(X_Uniform_Raw)
ax1.set_title('RAW Uniform.  (0,10)')
ax4.plot(X_Binomial_Raw)
ax4.set_title('RAW Binomial (n=10, p=0.5)')
ax7.plot(X_Geometric_Raw)
ax7.set_title('RAW Geometric (p=0.5)')


ax2.hist(X_Uniform_Raw, 30, density=True)
ax2.set_title('Uniform PMF')
ax5.hist(X_Binomial_Raw, 30, density=True)
ax5.set_title('Binomial PMF')
ax8.hist(X_Geometric_Raw, 30, density=True)
ax8.set_title('Geometric PMF')


ax3.plot(Uniform_Sorted, p1)
ax3.set_title('Uniform CDF')
ax6.plot(Binomial_Sorted, p2)
ax6.set_title('Binomial CDF')
ax9.plot(Geometric_Sorted, p3)
ax9.set_title('Geometric CDF')

plt.show()

