#Author: L. Pezzini
#Date: 3 Mar 2021

'''
This way of computing Nmin is clearly inefficient. For example, if we require err(Nmin) < 10−6. and we calculate err(2) = 0.02, 
it is a waste of time to calculate err(3) as it is already obvious that Nmin is very much larger than 2! 
Rewrite your program so that is uses a more efficient way to locate the minimum value of N. Your new method must produce exactly 
the same value for Nmin as before but should be faster. For example, you might try and reduce the number of times that you have to evaluate err(N). 
You should also tell us how much faster your new program is. 
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
N = 0 
it = 0
a = 1

while err > tol and a <= Nmax:
    it += 1
    a *= 2*it
    pi, err = pi_riemann(a)

print('Approximation of pi', pi_riemann(a))
print('Minimum number of iteration:', it)

err2 = 1.
while err2 > tol and N <= Nmax:
    pi, err2 = pi_riemann(N)
    N += 1

print(N)
print('This methos is ', N/it, 'time fatser than the one in ex2.')
