# Lab6
# Matthew Teears

# imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from scipy import stats

# definitions
nobs = 1000

Gaussian1 = np.random.normal(100, 10, nobs)
Gaussian2 = np.random.normal(0, 10, nobs)
Gaussian3 = np.random.normal(0, 1, nobs)

X1 = stats.norm(100, 10)
X2 = stats.norm(0, 10)
X3 = stats.norm(0, 1)

Gaussian1_sort = []
Gaussian2_sort = []
Gaussian3_sort = []

Gaussian1_sort = np.sort(Gaussian1)
Gaussian2_sort = np.sort(Gaussian2)
Gaussian3_sort = np.sort(Gaussian3)

p1 = np.arange(len(Gaussian1))/(len(Gaussian1) - 1)
p2 = np.arange(len(Gaussian2))/(len(Gaussian2) - 1)
p3 = np.arange(len(Gaussian3))/(len(Gaussian3) - 1)

Mean1 = np.mean(Gaussian1)
Mean2 = np.mean(Gaussian2)
Mean3 = np.mean(Gaussian3)

for x in Gaussian1:
    Y1 = x - Mean1

for x in Gaussian2:
    Y2 = x - Mean2

for x in Gaussian3:
    Y3 = x - Mean3


Std1 = np.std(Gaussian1, ddof=1)
Std2 = np.std(Gaussian2, ddof=1)
Std3 = np.std(Gaussian3, ddof=1)

print('\nStatistics for X~Gaussian(100, 100):')
print('Mean: ', Mean1)
print('SDev: ', Std1)
print('\nStatistics for X~Gaussian(0, 100):')
print('Mean: ', Mean2)
print('SDev: ', Std2)
print('\nStatistics for X~Gaussian(0, 1):')
print('Mean: ', Mean3)
print('SDev: ', Std3)

print('\nZ ~ Gaussian(0, 1):\n')
print('P[Z > 0]:        ', 1 - X3.cdf(0))
print('P[Z < 0]:        ', X3.cdf(0))
print('P[Z > 1]:        ', 1 - X3.cdf(1))
print('P[Z < -1]:       ', X3.cdf(-1))
print('P[Z > 2]:        ', 1 - X3.cdf(2))
print('P[Z < -2]:       ', X3.cdf(-2))
print('P[-1 < Z < 1]:   ', X3.cdf(1) - X3.cdf(-1))
print('P[-2 < Z < 2]:   ', X3.cdf(2) - X3.cdf(-2))

print('\nX ~ Gaussian(100, 100):\n')
print('P[X > 100]:        ', 1 - X1.cdf(100))
print('P[X < 100]:        ', X1.cdf(100))
print('P[X > 110]:        ', 1 - X1.cdf(110))
print('P[X < 90]:         ', X1.cdf(90))
print('P[X > 120]:        ', 1 - X1.cdf(120))
print('P[X < 80]:         ', X1.cdf(80))
print('P[90 < X < 110]:   ', X1.cdf(110) - X1.cdf(90))
print('P[80 < X < 120]:   ', X1.cdf(120) - X1.cdf(80))




fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, figsize=(15, 15))
fig.suptitle('Lab 6. Teears', fontsize=16)

ax1.plot(Gaussian1)
ax1.set_title('X~Gaussian(100, 100)')
ax4.plot(Gaussian2)
ax4.set_title('X~Gaussian(0, 100)')
ax7.plot(Gaussian3)
ax7.set_title('X~Gaussian(0, 1)')

ax2.hist(Gaussian1, 30, density=True)
ax2.set_title('PMF X~Gaussian(100, 100)')
ax5.hist(Gaussian2, 30, density=True)
ax5.set_title('PMF X~Gaussian(0, 100)')
ax8.hist(Gaussian3, 30, density=True)
ax8.set_title('PMF X~Gaussian(0, 1)')

ax3.plot(Gaussian1_sort, p1)
ax3.set_title('CDF X~Gaussian(100, 100)')
ax6.plot(Gaussian2_sort, p2)
ax6.set_title('CDF X~Gaussian(0, 100)')
ax9.plot(Gaussian3_sort, p3)
ax9.set_title('CDF X~Gaussian(0, 1)')

plt.show()

