import operator


def to_repr(func_name, **kwargs):
    args_repr = ', '.join(f'{k}={v!r}' for k, v in kwargs.items() if v is not None)
    return f'{func_name}({args_repr})'


def op2str(op):
    return {
        operator.add: '+',
        operator.sub: '-',
        operator.mul: '*',
        operator.truediv: '/',
        operator.pow: '**'
    }[op]
