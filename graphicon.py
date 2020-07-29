from matplotlib import pyplot as pl
from model.parser import Parser, real
import numpy as np


def null_line(x):
    return 0


def complex_plot(expressions: str):
    arr = np.arange(-5., 5., 0.02, dtype='complex_')

    p = Parser(expressions)

    f1 = np.vectorize(p.real_exec, otypes=[complex])
    f2 = np.vectorize(p.imag_exec, otypes=[complex])
    nf = np.vectorize(null_line, otypes=[complex])

    fig, ax = pl.subplots()

    ax.plot(arr, nf(arr), color='green')
    ax.plot(nf(arr), arr, color='green')
    ax.plot(f1(arr), f2(arr), color='blue')

    pl.grid(True)

    pl.show()


def fun_plot(expressions: str):
    arr = np.arange(-5., 5., 0.02, dtype='complex_')

    p = Parser(expressions)

    f1 = np.vectorize(p.real_exec, otypes=[complex])
    f2 = np.vectorize(p.imag_exec, otypes=[complex])
    nf = np.vectorize(null_line, otypes=[complex])

    fig, ax = pl.subplots()

    ax.plot(arr, nf(arr), color='green')
    ax.plot(nf(arr), arr, color='green')
    ax.plot(arr, f1(arr), color='red')

    pl.grid(True)

    fig.savefig("plot.png")

    pl.show()


fun = input("Input yout function: ")

fun_plot(fun)
complex_plot(fun)
