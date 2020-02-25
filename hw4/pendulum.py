#!/usr/bin/env python
# MATH 481 problem 3

import sys
import numpy as np
import matplotlib
import matplotlib.pylab as plt

def linTSM2(eta, d_eta, N, g, L):
    # the second-order differential eq is modeled as a system:
    #
    # u1 = theta
    # u1' = u2 = theta'
    # u2' = theta'' = -g/L * u1
    # u1'' = u2' = theta''
    # u2'' = d/dt (-g/L * u1) = -g/L * (u2)
    #
    # returns t[], u1[], u2[]

    k = 4 / N
    t = np.zeros(N+1)
    u1 = np.zeros(N+1)
    u2 = np.zeros(N+1)

    def d1u1(n):
        return u2[n]

    def d2u1(n):
        return d1u2(n)

    def d1u2(n):
        return (-g/L)*u1[n]

    def d2u2(n):
        return (-g/L)*u2[n]

    u1[0] = eta
    u2[0] = d_eta

    for i in range(N+1):
        t[i] = k * i

    for n in range(N):
        u1[n+1] = u1[n] + k * d1u1(n) + (1/2)*(k ** 2)*d2u1(n)
        u2[n+1] = u2[n] + k * d1u2(n) + (1/2)*(k ** 2)*d2u2(n)

    return t, u1, u2

def main():
    plt.figure(1)
    plt.clf()
    plt.grid()
    plt.title('Taylor series method approximations')

    def exact_theta(t, eta, d_eta):
        c1 = d_eta / 4.01061
        c2 = eta

        return c1 * np.sin(4.01061*t) + c2 * np.cos(4.01061*t)

    def exact_dtheta(t, eta, d_eta):
        c1 = d_eta / 4.01061
        c2 = eta

        return 4.01061 * c1 * np.cos(4.01061*t) - 4.01061 * c2 * np.sin(4.01061*t)

    results = []

    for N in [40, 80, 160, 320, 640, 1280, 2560]:
        t, u1, u2 = linTSM2(np.pi/6, 0, N, 32.17, 2)

        err = abs(u1[N] - exact_theta(4, np.pi/6, 0))
        derr = abs(u2[N] - exact_dtheta(4, np.pi/6, 0))

        print('N={0}, u1[N]={1}'.format(N, u1[N]))

        results.append({
            'N': N,
            'k': 4/N,
            'err': err,
            'ratio': '-' if N == 40 else results[-1]['err'] / err,
            'derr': derr,
            'dratio': '-' if N == 40 else results[-1]['derr'] / derr,
        })

    for r in results:
        print('N: {5}, k: {0}, err: {1}, ratio: {2}, derr: {3}, dratio: {4}'.format(r['k'], r['err'], r['ratio'], r['derr'], r['dratio'], r['N']))

    return 0

if __name__ == '__main__':
    sys.exit(main())
