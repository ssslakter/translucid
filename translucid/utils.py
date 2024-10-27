import torch
import operator

__all__ = ['to_repr', 'op2str', 'to_cpu', 'to_device', 'default_device']


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


def to_cpu(x: torch.Tensor): return x.cpu().detach()

default_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def to_device(x: torch.Tensor, device=default_device): 
    return x.to(device)