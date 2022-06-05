from __future__ import division
import math
import operator as op
from typing import Union, Any


class Sexp:
    # A Lisp Symbol is implemented as a Python str
    Symbol = str
    # A Lisp List is implemented as a Python list
    List = list
    # A Lisp Number is implemented as a Python int or float
    Number = (int, float)

    def __init__(self) -> None:
        self.global_env = self.standard_env()

    def atom(self, token: str) -> Union[int, float, str]:
        """Numbers become numbers; every other token is a symbol."""
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return self.Symbol(token)

    def read_from_tokens(self, tokens: list) -> Union[list, int, float, str]:
        """Read an expression from a sequence of tokens."""
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF while reading')
        token = tokens.pop(0)
        if '(' == token:
            line = []
            while tokens[0] != ')':
                line.append(self.read_from_tokens(tokens))
            tokens.pop(0)  # pop off ')'
            return line
        elif ')' == token:
            raise SyntaxError('unexpected )')
        else:
            return self.atom(token)

    def parse(self, program: str) -> Union[list, int, float, str]:
        """Read a Scheme expression from a string."""
        return self.read_from_tokens(self.tokenize(program))

    def tokenize(self, s: str) -> list:
        """Convert a string into a list of tokens."""
        return s.replace('(', ' ( ').replace(')', ' ) ').split()

    # Environments
    def standard_env(self) -> 'Env':
        """An environment with some Scheme standard procedures."""
        env = Env()
        env.update(vars(math))  # sin, cos, sqrt, pi, ...
        env.update({
            '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv,
            '>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '=': op.eq,
            'print': print,
            'and': op.and_,
            'or': op.or_,
            'not': op.not_,
        })
        return env

    # eval
    def eval(self, x: Union[str, list], env=None) -> Any:
        """Evaluate an expression in an environment."""
        if env is None:
            env = self.global_env
        if isinstance(x, self.Symbol):  # variable reference
            return env.find(x)[x]
        elif not isinstance(x, self.List):  # constant literal
            return x
        elif x[0] == 'if':  # (if test conseq alt)
            (_, test, conseq, alt) = x
            exp = (conseq if self.eval(test, env) else alt)
            return self.eval(exp, env)
        elif x[0] == 'define' or x[0] == 'print':  # (define var exp)
            (_, var, exp) = x
            env[var] = self.eval(exp, env)
        elif x[0] == 'lambda':  # (lambda (var...) body)
            (_, parms, body) = x
            return Procedure(parms, body, env)
        else:  # (proc arg...)
            proc = self.eval(x[0], env)
            args = [self.eval(exp, env) for exp in x[1:]]
            # print("proc: ",proc,", *args: ",args)
            return proc(*args)


class Env(dict):
    """The environment is a dictionary with {'var':val} as the key pair,
    and it also carries a reference to the outer environment."""

    def __init__(self, parms=(), args=(), outer=None) -> None:
        super(Env, self).__init__()
        self.update(zip(parms, args))
        self.outer = outer

    def find(self, var: str) -> 'Env':
        """Find the innermost Env where var appears."""
        if var in self:
            return self
        elif self.outer is not None:
            return self.outer.find(var)
        else:
            raise AttributeError("This arithmetic symbol does not exist")


class Procedure(object):
    """A user-defined Scheme procedure."""
    def __init__(self, parms: str, body: str, env: 'Env') -> None:
        self.parms, self.body, self.env = parms, body, env
        self.exp = Sexp()

    def __call__(self, *args: str) -> Any:
        return self.exp.eval(self.body, Env(self.parms, args, self.env))
