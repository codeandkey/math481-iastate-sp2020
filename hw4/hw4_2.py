#!/usr/bin/env python
# MATH 481 HW4 problem 2

import numpy as np
import matplotlib
import matplotlib.pylab as plt
import sys

def compute(N):
    out = np.zeros(N+1)
    t = np.zeros(N + 1)

    # define derivative functions for expansion
    def d1(x):
        return -(np.e ** x) + 2*x + 2

    def d2(x):
        return -(np.e ** x) + 2

    def d3(x):
        return -(np.e ** x)

    def d4(x):
        return -(np.e ** x)

    k = 2 / N

    # compute t[n] table for better readability
    for n in range(N + 1):
        t[n] = k * n

    for n in range(N):
        out[n + 1] = out[n] + k * d1(t[n]) + (1/2)*(k**2)*d2(t[n]) + (1/6)*(k**3)*d3(t[n]) + (1/24)*(k**4)*d4(t[n])

    return t, out

def main():
    matplotlib.rcParams.update({
        'font.size': '14',
        'font.family': 'serif',
        'text.usetex': 'true',
    })

    def y(x):
        return -(np.e ** x) + x ** 2 + 2 * x + 1

    xorig = np.linspace(0, 2, 100)

    plt.figure(1)
    plt.clf()
    plt.grid()
    plt.title('Taylor series method plots')

    plt.plot(xorig, y(xorig), 'r-')

    plt.xlabel('x')
    plt.ylabel('y')

    results = []

    for j in range(3, 11):
        N = 2**j
        t, U = compute(N)
        err = abs(U[N] - y(2))
        results.append({
            'k': 2/N,
            'error': err,
            'ratio': '-' if j == 3 else results[-1]['error'] / err,
        })

    for i in results:
        print('k: {0}, err: {1}, ratio: {2}'.format(i['k'], i['error'], i['ratio']))

    return 0

if __name__ == '__main__':
    sys.exit(main())
