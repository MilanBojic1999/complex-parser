import cmath as cm
import collections

_Constants = {
    'pi': cm.pi,
    'Pi': cm.pi,
    'PI': cm.pi,
    'e': cm.e,
    'phi': (1 + 5 ** .5) / 2,
    'i': cm.sqrt(-1)

}


def iden(x):
    return x


def mypow(x, p):
    return x ** p


def real(x):
    if type(x) == complex:
        return x.real
    return x


def imag(x):
    if type(x) == complex:
        return x.imag
    return 0


_Variables = ('x', 'y', 'z', 't')

_Operation = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,

}

_Functions = {
    'real': real,
    'imag': imag,
    'abs': abs,
    'pow': mypow,
    'sqrt': cm.sqrt,
    'exp': cm.exp,
    'log': cm.log,
    'cos': cm.cos,
    'sin': cm.sin,
    'tan': cm.tan
}

local = {**_Constants, **_Functions}


class Parser:
    def __init__(self, expr: str):
        self.expr = expr

    def exec(self, x):
        if isinstance(x,collections.Hashable) and x in _Constants.keys():
            x = _Constants.get(x)
        local['x'] = x
        return eval(self.expr, local)

    def real_exec(self,x):
        return real(self.exec(x))

    def imag_exec(self,x):
        return imag(self.exec(x))
