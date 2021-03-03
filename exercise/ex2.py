#Author: L. Pezzini
#Date: 3 Mar 2021

'''
We now want to find out the minimum value of N that is required to give a value for π(N) that is accurate to some specified value. We will call this value Nmin. 
By computing π(N) for increasing values of N, calculate Nmin such that err(Nmin) < 10−6 
'''
import numpy as np
import sys

# Better method: using Riemans series
def pi_riemann(N):
    pigreco = np.float
    err = np.float
    pigreco = 0.
    err = 0.
    for k in range(0, N):
        pigreco += (2*pow(-1, k)*pow(3, 0.5-k))/(2*k+1)
    err = np.abs(pigreco - np.pi)/np.pi
    return pigreco, err


# Picard iteration
err = 1.
tol = 1e-6
Nmax = 100
N = 1

while err > tol and N <= Nmax:
    pi, err = pi_riemann(N)
    N += 1

print('Approximation of pi', pi_riemann(N))
print('Minimum number of iteration:', N)
