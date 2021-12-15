import argparse
from generator import ExprGenerator, OPERATORS, NEGATION
from metaheuristic import run
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-len", type=int, required=False,
    help="length of random generated expression")
parser.add_argument("-expr", type=str, required=False,
    help="boolean expression")
args = parser.parse_args()
len = args.len
expr = args.expr

if len is not None:
    # random expression generation.
    gen = ExprGenerator()
    expr = gen.genExpr(len)
    vars = list(set(gen.vars))
else:
    # manual expression input.
    split_expr = expr.split(' ')
    vars = []
    for e in split_expr:
        if e is not NEGATION and e not in OPERATORS:
            vars.append(str(e))

ordering = run(expr, vars)
ordering_txt = ' '.join(ordering)
print(ordering_txt)