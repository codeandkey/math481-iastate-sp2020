#!/usr/bin/env python
#
# MATH 481 - HW2 Q1 source code.
# Justin Stanley
# Feb 4, 2020

import sys
import matplotlib
import matplotlib.pylab as plt
import numpy as np

PLOT_STEPS = 1000

def compute_taylor(x, n):
    size = len(x)
    out = np.zeros(size)

    assert(n >= 0 and n <= 3)

    for i in range(size):
        # f(pi/4) = 3tan(pi/4)
        out[i] = 3.0

        if n > 0:
            # f'(pi/4) = 3sec^2(pi/4)
            out[i] += 6 * (x[i] - np.pi / 4)

            if n > 1:
                # f''(pi/4) = 6tan(pi/4)sec^2(pi/4) = 12
                out[i] += 6 * (x[i] - np.pi / 4) ** 2

                if n > 2:
                    # f'''(pi/4) = 6(sec^4(pi/4) + 2tan^2(pi/4) sec^2(pi/4)) = 48
                    out[i] += 8 * (x[i] - np.pi / 4) ** 3

    return out

def main():
    matplotlib.rcParams.update({
        'font.size': 14,
        'font.family': 'serif',
        'text.usetex': 'true',
    })

    x = np.linspace(np.pi / 12.0, 5 * np.pi / 12, PLOT_STEPS)

    def f(x):
        return 3 * np.tan(x)

    y = f(x)

    p1 = compute_taylor(x, 1)
    p2 = compute_taylor(x, 2)
    p3 = compute_taylor(x, 3)

    plt.figure(1)
    plt.clf()
    plt.grid()
    plt.title('Taylor polynomial approximations of f(x) = 3 tan(x)')

    plt.plot(x, y, 'r-')
    plt.plot(x, p1, 'g-')
    plt.plot(x, p2, 'b-')
    plt.plot(x, p3, 'c-')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend(['f(x)', 'P1(x)', 'P2(x)', 'P3(x)'])
    plt.axis([np.pi/12, 5 * np.pi/12, 0, 10])
    plt.show()

    return 0

if __name__ == '__main__':
    sys.exit(main())
