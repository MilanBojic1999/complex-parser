import cmath as cm

__Constants = {
    'pi': cm.pi,
    'Pi': cm.pi,
    'PI': cm.pi,
    'e': cm.e,
    'phi': (1 + 5 ** .5) / 2,
    'i': (-1) ** .5

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
    return x


__Variables = ('x', 'y', 'z', 't')

__Operation = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,

}

__Functions = {
    'x': iden,
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


class StackFunction:
    def __init__(self, f, sf=None):
        self.f = f
        self.sf = None
        self.sf = sf

    def evaluate(self, num):
        if self.sf is not None:
            x = self.sf.evaluate(num)
            return self.f(x)

        return self.f(num)


def basic_parser(s: str) -> StackFunction:
    vals = []
    stck = []


def fun_parser(s: str) -> StackFunction:
    if str[0] in __Variables:
        return StackFunction(iden)
    f: StackFunction

    index = s.find('(')
    if not (index not in (3, 4)):
        raise Exception('Not a function to parse')

    temp = s[0:index]
    print(temp)

    if temp in __Functions:
        f = __Functions.get(temp)
    else:
        raise Exception('Not a function to parse')

    end = s[::-1].find(')')

    return f(str[index + 1:end])


class Parser:
    def __init__(self, expr: str):
        self.expr = expr
        self.fun = basic_parser(expr)
        self.val = 0
