from model.parser import Parser, li
from graphicon import complex_plot, fun_plot
import numpy as np
from matplotlib.figure import Figure


def transformation(fun: str, arr: np.ndarray):
    p = Parser(fun)

    try:
        p.exec(0)
    except Exception:
        return
    else:

        fig = complex_plot(p, arr)

        fig.savefig("output.png")


def input_function(fun: str, in_zoom: float = 1.0, out_zoom: float = 1.0):
    p = Parser(fun)

    try:
        p.exec(0)
    except Exception:
        return None

    arr = np.arange(-10 * in_zoom, 10 * in_zoom, 0.02)

    out_arr = np.arange(-10 * out_zoom, 10 * out_zoom, 0.02)

    vf = np.vectorize(p.real2complex, otypes=[complex])

    res = vf(out_arr)

    fig = fun_plot(p, arr)

    fig.savefig("input.png")

    return res
