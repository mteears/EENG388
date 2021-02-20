# Lab6
# Matthew Teears

# imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from scipy import stats

# definitions
nobs = 1000

Gaussian1_X1 = np.random.normal(0, 10, nobs)
Gaussian1_Y1 = np.random.normal(0, 10, nobs)
Gaussian1_W = Gaussian1_X1 + Gaussian1_Y1

Gaussian2_X2 = np.random.normal(10, 10, nobs)
Gaussian2_Y2 = np.random.normal(20, 10, nobs)
Gaussian2_W = Gaussian2_X2 + Gaussian2_Y2


Gaussian3_X3 = np.random.normal(10, 10, nobs)
Gaussian3_X4 = np.random.normal(10, 10, nobs)
Gaussian3_X5 = np.random.normal(10, 10, nobs)
Gaussian3_X6 = np.random.normal(10, 10, nobs)
Gaussian3_X7 = np.random.normal(10, 10, nobs)
Gaussian3_W = Gaussian3_X3 + Gaussian3_X4 + Gaussian3_X5 + Gaussian3_X6 + Gaussian3_X7

Uniform_X1 = np.random.uniform(0, 10, nobs)
Uniform_X2 = np.random.uniform(0, 10, nobs)
Uniform_X3 = np.random.uniform(0, 10, nobs)
Uniform_X4 = np.random.uniform(0, 10, nobs)
Uniform_X5 = np.random.uniform(0, 10, nobs)
Uniform_W = Uniform_X1 + Uniform_X2 + Uniform_X3 + Uniform_X4 + Uniform_X5

Binomial_X1 = np.random.binomial(10, 0.5, nobs)
Binomial_X2 = np.random.binomial(10, 0.5, nobs)
Binomial_X3 = np.random.binomial(10, 0.5, nobs)
Binomial_X4 = np.random.binomial(10, 0.5, nobs)
Binomial_X5 = np.random.binomial(10, 0.5, nobs)
Binomial_W = Binomial_X1 + Binomial_X2 + Binomial_X3 + Binomial_X4 + Binomial_X5

Geometric_X1 = np.random.geometric(0.5, nobs)
Geometric_X2 = np.random.geometric(0.5, nobs)
Geometric_X3 = np.random.geometric(0.5, nobs)
Geometric_X4 = np.random.geometric(0.5, nobs)
Geometric_X5 = np.random.geometric(0.5, nobs)
Geometric_X6 = np.random.geometric(0.5, nobs)
Geometric_X7 = np.random.geometric(0.5, nobs)
Geometric_X8 = np.random.geometric(0.5, nobs)
Geometric_X9 = np.random.geometric(0.5, nobs)
Geometric_X10 = np.random.geometric(0.5, nobs)
Geometric_W1 = Geometric_X1 + Geometric_X2 + Geometric_X3 + Geometric_X4 + Geometric_X5
Geometric_W2 = Geometric_X1 + Geometric_X2 + Geometric_X3 + Geometric_X4 + Geometric_X5 + Geometric_X6 + Geometric_X7 + Geometric_X8 + Geometric_X9 + Geometric_X10


Gaussian1_sort = []
Gaussian2_sort = []
Gaussian3_sort = []
Uniform_sort = []
Binomial_sort = []
Geometric_sort = []

Gaussian1_W_sort = np.sort(Gaussian1_W)
Gaussian2_W_sort = np.sort(Gaussian2_W)
Gaussian3_W_sort = np.sort(Gaussian3_W)
Uniform_W_sort = np.sort(Uniform_W)
Binomial_W_sort = np.sort(Binomial_W)
Geometric_W1_sort = np.sort(Geometric_W1)
Geometric_W2_sort = np.sort(Geometric_W2)


p1 = np.arange(len(Gaussian1_W))/(len(Gaussian1_W) - 1)
p2 = np.arange(len(Gaussian2_W))/(len(Gaussian2_W) - 1)
p3 = np.arange(len(Gaussian3_W))/(len(Gaussian3_W) - 1)
p4 = np.arange(len(Uniform_W))/(len(Uniform_W) - 1)
p5 = np.arange(len(Binomial_W))/(len(Binomial_W) - 1)
p6 = np.arange(len(Geometric_W1))/(len(Geometric_W1) - 1)
p7 = np.arange(len(Geometric_W2))/(len(Geometric_W2) - 1)

Mean1 = np.mean(Gaussian1_W)
Mean2 = np.mean(Gaussian2_W)
Mean3 = np.mean(Gaussian3_W)
Mean_Uniform = np.mean(Uniform_W)
Mean_Binomial = np.mean(Binomial_W)
Mean_Geometric1 = np.mean(Geometric_W1)
Mean_Geometric2 = np.mean(Geometric_W2)

Std1 = np.std(Gaussian1_W, ddof=1)
Std2 = np.std(Gaussian2_W, ddof=1)
Std3 = np.std(Gaussian3_W, ddof=1)
Std_Uniform = np.std(Uniform_W, ddof=1)
Std_Binomial = np.std(Binomial_W, ddof=1)
Std_Geometric1 = np.std(Geometric_W1, ddof=1)
Std_Geometric2 = np.std(Geometric_W2, ddof=1)

VAR1 = np.var(Gaussian1_W)
VAR2 = np.var(Gaussian2_W)
VAR3 = np.var(Gaussian3_W)
VAR_Uniform = np.var(Uniform_W)
VAR_Binomial = np.var(Binomial_W)
VAR_Geometric1 = np.var(Geometric_W1)
VAR_Geometric2 = np.var(Geometric_W2)


print('\n W = X + Y w/ X,Y ~ Gaussian(0, 100)')
print('Mean: ', Mean1)
print('SDev: ', Std1)
print('VAR : ', VAR1)
print('\nX ~ Gaussian(10, 100) ; Y ~ Gaussian(20, 100)')
print('Mean: ', Mean2)
print('SDev: ', Std2)
print('VAR : ', VAR2)
print('\nSUM Xi ~ Gaussian(10, 100):')
print('Mean: ', Mean3)
print('SDev: ', Std3)
print('VAR : ', VAR3)
print('\nSUM Xi ~ Uniform(0, 10):')
print('Mean: ', Mean_Uniform)
print('SDev: ', Std_Uniform)
print('VAR : ', VAR_Uniform)
print('\nSUM Xi ~ Binomial(10, 0.5):')
print('Mean: ', Mean_Binomial)
print('SDev: ', Std_Binomial)
print('VAR : ', VAR_Binomial)
print('\nSUM Xi ~ Geometric(0.5):')
print('Mean: ', Mean_Geometric1)
print('SDev: ', Std_Geometric1)
print('VAR : ', VAR_Geometric1)
print('\nSUM Xi ~ Geometric(0.5):')
print('Mean: ', Mean_Geometric2)
print('SDev: ', Std_Geometric2)
print('VAR : ', VAR_Geometric2)


fig1, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, figsize=(15, 15))
fig1.suptitle('Lab 6. Teears 1', fontsize=16)
ax1.plot(Gaussian1_W)
ax1.set_title('RAW W=X+Y w/ X,Y ~ Gaussian(0, 10)')
ax4.plot(Gaussian2_W)
ax4.set_title('RAW W=X+Y; X ~ Gaussian(10, 100) ; Y ~ Gaussian(20, 100)')
ax7.plot(Gaussian3_W)
ax7.set_title('RAW W w/ Xi ~ Gaussian(10, 100')
ax2.hist(Gaussian1_W, 30, density=True)
ax2.set_title('PMF ~ Gaussian (0, 10)')
ax5.hist(Gaussian2_W, 30, density=True)
ax5.set_title('PMF X~Gaussian(10, 100 ; Y ~ Gaussian(20, 100)')
ax8.hist(Gaussian3_W, 30, density=True)
ax8.set_title('PMF Xi ~ Gaussian(10, 100')
ax3.plot(Gaussian1_W_sort, p1)
ax3.set_title('CDF ~ Gaussian (0, 10)')
ax6.plot(Gaussian2_W_sort, p2)
ax6.set_title('CDF X~Gaussian(10, 100 ; Y ~ Gaussian(20, 100)')
ax9.plot(Gaussian3_W_sort, p3)
ax9.set_title('CDF Xi ~ Gaussian(10, 100')
plt.show()

fig2, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12)) = plt.subplots(4, 3, figsize=(15, 15))
fig2.suptitle('Lab 6. Teears 2', fontsize=16)
ax1.plot(Uniform_W)
ax1.set_title('RAW X ~ Uniform(0, 10)')
ax4.plot(Binomial_W)
ax4.set_title('RAW X ~ Binomial(10, 0.5)')
ax7.plot(Geometric_W1)
ax7.set_title('RAW X ~ Geometric(0.5)')
ax10.plot(Geometric_W2)
ax10.set_title('RAW X ~ Geometric(0.5)')
ax2.hist(Uniform_W, 30, density=True)
ax2.set_title('PMF X ~ Uniform(0, 10)')
ax5.hist(Binomial_W, 30, density=True)
ax5.set_title('PMF X ~ Binomial(10, 0.5)')
ax8.hist(Geometric_W1, 30, density=True)
ax8.set_title('PMF X ~ Geometric(0.5)')
ax11.hist(Geometric_W2, 30, density=True)
ax11.set_title('PMF X ~ Geometric(0.5)')
ax3.plot(Uniform_W_sort, p4)
ax3.set_title('CDF X ~ Uniform(0, 10')
ax6.plot(Binomial_W_sort, p5)
ax6.set_title('CDF X ~ Binomial(10, 0.5)')
ax9.plot(Geometric_W1_sort, p6)
ax9.set_title('CDF X1..X5 ~ Geometric(0.5)')
ax12.plot(Geometric_W2_sort, p7)
ax12.set_title('CDF X1..X10 ~ Geometric(0.5)')
plt.show()