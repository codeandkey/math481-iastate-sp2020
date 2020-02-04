#!/usr/bin/env python
#
# MATH 481 - HW2 Q6 source code.
# Justin Stanley
# Feb 4, 2020

import sys
import matplotlib
import matplotlib.pylab as plt
import numpy as np

PLOT_STEPS = 1000

def Newton(f, df, x0, N):
    if N == 0:
        return x0

    prev = Newton(f, df, x0, N - 1)

    return prev - f(prev)/df(prev)

def main():
    def f(x):
        return np.e ** x - x ** 2 + 3 * x - 2

    def df(x):
        return np.e ** x - 2 * x + 3

    n = 0
    while True:
        res = Newton(f, df, -0.5, n)

        print('n={0}, res = {1}, f(res) = {2}'.format(n, res, f(res)))

        if abs(f(res)) < 10 ** -12:
            print('Found sufficiently large n={0} => x_n = {1}, f(x_n) = {2}'.format(n, res, f(res)))
            break

        n += 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
