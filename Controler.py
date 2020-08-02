from model.parser import Parser, li
from graphicon import complex_plot, fun_plot
import numpy as np
from matplotlib.figure import Figure


def transformation(fun: str, arr: np.ndarray):
    p = Parser(fun)

    fig = complex_plot(p, arr)

    fig.savefig("output.png")


def input_function(fun: str, in_zoom: float = 1.0, out_zoom: float = 1.0) -> np.ndarray:
    p = Parser(fun)

    arr = np.arange(-10 * in_zoom, 10 * in_zoom, 0.02)

    out_arr = np.arange(-10 * out_zoom, 10 * out_zoom, 0.02)

    vf = np.vectorize(p.real2complex, otypes=[complex])

    print(vf(2 * li), fun)

    res = vf(out_arr)

    fig = fun_plot(p, arr)

    fig.savefig("input.png")

    return res
