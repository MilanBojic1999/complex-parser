import cmath as cm
import collections

_Constants = {
    'pi': cm.pi,
    'Pi': cm.pi,
    'PI': cm.pi,
    'e': cm.e,
    'phi': (1 + 5 ** .5) / 2,
    'i': complex(0, 1)
}

li = _Constants['i']


def identity(x):
    return x


def power(x, p):
    return x ** p


def real(x) -> float:
    if type(x) == complex:
        return x.real
    return x


def imag(x) -> float:
    if type(x) == complex:
        return x.imag
    return 0.0


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
    'pow': power,
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

    def exec(self, x) -> complex:
        if isinstance(x, collections.Hashable) and x in _Constants.keys():
            x = _Constants.get(x)
        local['x'] = x
        try:
            cmp = eval(self.expr, local)
        except Exception:
            raise Exception
        else:
            return cmp

    def real_exec(self, x) -> float:
        return real(self.exec(x))

    def imag_exec(self, x) -> float:
        return imag(self.exec(x))

    def real2complex(self, x) -> complex:
        return x + self.exec(x) * li
