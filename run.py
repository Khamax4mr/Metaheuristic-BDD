from generator import ExprGenerator, OPERATORS, NEGATION
from metaheuristic import run
from sys import argv


if len(argv) < 2:
    # random formula generation.
    gen = ExprGenerator()
    expr = gen.genExpr(25)
    vars = gen.vars
else:
    expr = argv[1]
    split_expr = expr.split(' ')
    vars = []
    for e in split_expr:
        if e is not NEGATION and e not in OPERATORS:
            vars.append(str(e))

ordering = run(expr, vars)
for i in ordering:
    print(i)