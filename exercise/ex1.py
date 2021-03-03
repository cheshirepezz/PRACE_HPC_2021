#Author: L. Pezzini
#Date: 3 Mar 2021

'''
Write a program in C, C++, Fortran, Java or Python that computes an approximation to π using the above formula 
for the following values of N: 1, 2, 10, 50, 100, 500. For each value of N, print out the approximate value π(N) 
and the error err(N). The error is the difference between π(N) and the true value of π, ie err(N) = π(N) − π. 
As N increases the value of the error should decrease. 
'''

import numpy as np
import sys

'''
#THIS APPROX. IS NOT WORKING WELL!
def pi_approx(a):
    pigreco = np.float
    err = np.float
    pigreco = 0.
    err = 0.
    for i in range(1,a): 
        pigreco += 1./(1.+(i-0.5/a)**2) 
        #print(pigreco)
    pigreco *= (4./a) 
    err = pigreco - np.pi
    return pigreco, err

N = [1, 2, 10, 50, 100, 500]

for i in range(0, len(N)):
    print('Approximation for N =', N[i], '->', pi_approx(N[i]))

'''

# Better method: using Riemans series
def pi_riemann(N):
    pigreco = np.float64
    err = np.float64
    pigreco = 0.
    err = 0.
    for k in range(0, N):
        pigreco += (2*pow(-1,k)*pow(3,0.5-k))/(2*k+1)
    err = np.abs(pigreco - np.pi)/np.pi
    return pigreco, err

N = [1, 2, 10, 50, 100, 500]

for i in range(0, len(N)):
    print('Approximation for N =', N[i], '->', pi_riemann(N[i]))
