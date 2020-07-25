import cmath as cm

__Constants = {
    'pi': cm.pi,
    'Pi': cm.pi,
    'PI': cm.pi,
    'e': cm.e,
    'phi': (1 + 5 ** .5) / 2,
    'i': (-1) ** .5

}


def mypow(x, p):
    return x ** p


def real(x):
    if type(x) == complex:
        return x.real
    return x


def imag(x):
    if type(x) == complex:
        return x.imag
    return x


__Functions = {
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


class Parser:
    def __init__(self, expr: str):
        self.expr = expr

    def basic_parser(self, s: str):
        pass

    def fun_parser(self, s: str):
        pass
