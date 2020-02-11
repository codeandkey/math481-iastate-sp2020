#!/usr/bin/env python
# MATH 481 Spring 2020
# Homework 3, question 4-6

import sys
import matplotlib
import matplotlib.pylab as plt
import numpy as np

def euler_k(f, eta, T, k):
    # shorthand for euler, with a k value given instead of N
    return euler(f, eta, T, int(T / k))

def euler(f, eta, T, N):
    k = T / N

    t = [0]
    U = [eta]

    for n in range(1, N + 1):
        U.append(U[-1] + k * f(t[-1], U[-1]))
        t.append(t[-1] + k)

    return t, U

def main():
    matplotlib.rcParams.update({
        'font.size': 14,
        'font.family': 'serif',
        'text.usetex': 'true',
    })

    plt.figure(1)
    plt.clf()
    plt.grid()
    plt.title('Euler method approximating a nonlinear equation')

    def f(t, u):
        return 2 * t * (1 + u)

    # (problem 5)
    actual = np.e ** 4 - 1
    elist = [0] * 12
    for m in range(1, 11):
        k = 0.1 * (2 ** -m)
        t, U = euler_k(f, 0, 2, k)
        elist[m] = np.abs(actual - U[-1])

        print('===> k: {0}'.format(k))
        print('UN = {0}'.format(U[-1]))
        print('Ek = {0}'.format(elist[m]))
        print('E2k/Ek = {0}'.format(elist[m-1]/elist[m]))

    # (problem 6)

    def nonlinear_f(t, u):
        return -5 * u + 5 * np.cos(t * u)

    colors = [ 'r', 'g', 'b', 'c' ]
    for i in range(0, 4):
        k = 0.4 / (2 ** i)
        t, U = euler_k(nonlinear_f, 1, 10, k)

        plt.plot(t, U, '{0}-o'.format(colors[i]))

    plt.xlabel('t')
    plt.ylabel('U')
    plt.legend(['k=0.4', 'k=0.2', 'k=0.1', 'k=0.05'])
    plt.savefig('q6.png', dpi=300)

    return 0

if __name__ == '__main__':
    sys.exit(main())
