from matplotlib import pyplot as pl
from matplotlib.figure import Figure

from model.parser import Parser
import numpy as np


def null_line(x):
    return 0


def complex_plot(p: Parser, arr: np.ndarray = np.arange(-5., 5., 0.02, dtype='complex_')):
    # arr = np.arange(-5., 5., 0.02, dtype='complex_')

    f1 = np.vectorize(p.real_exec, otypes=[complex])
    f2 = np.vectorize(p.imag_exec, otypes=[complex])
    nf = np.vectorize(null_line, otypes=[complex])

    fig, ax = pl.subplots()

    min = np.amin(f2(arr))
    max = np.amax(f2(arr))

    zeros = np.linspace(min, max, 100)

    print(zeros)

    ax.plot(arr, nf(arr), color='green')
    ax.plot(nf(zeros), zeros, color='green')
    ax.plot(f1(arr), f2(arr), color='blue')

    pl.grid(True)

    # pl.show()

    return fig


def fun_plot(p: Parser, arr: np.ndarray = np.arange(-5., 5., 0.02, dtype='complex_')) -> Figure:
    f1 = np.vectorize(p.real_exec, otypes=[complex])
    f2 = np.vectorize(p.imag_exec, otypes=[complex])
    nf = np.vectorize(null_line, otypes=[complex])

    fig, ax = pl.subplots()

    min = np.amin(f1(arr))
    max = np.amax(f1(arr))


    zeros = np.linspace(min, max, 100)


    ax.plot(arr, nf(arr), color='green')
    ax.plot(nf(zeros), zeros, color='green')
    ax.plot(arr, f1(arr), color='red')

    pl.grid(True)

    # pl.show()

    return fig

# fun = input("Input yout function: ")
#
# fg1 = fun_plot(fun)
# fg1.savefig("view/input.png")
#
# fg2 = complex_plot(fun)
# fg2.savefig("view/output.png")
