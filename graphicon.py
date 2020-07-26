from matplotlib import pyplot as pl
from model.parser import Parser, real
import numpy as np


def null_line(x):
    return 0


fun = input('Put your function: ')

arr = np.arange(-10., 10., 0.02)

p = Parser(fun)

f1 = np.vectorize(p.real_exec)
f2 = np.vectorize(p.imag_exec)
nf = np.vectorize(null_line)

fig, ax = pl.subplots()

ax.plot(arr, nf(arr),color = 'green')
ax.plot(nf(arr), arr,color = 'green')
ax.plot(f1(arr), f2(arr),color = 'blue')
#ax.plot(arr, f1(arr),color = 'red')

pl.grid(True)

pl.show()
