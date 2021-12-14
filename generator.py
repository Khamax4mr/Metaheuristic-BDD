# random formula generator.
from random import randint, choice

# this system follows pyeda's boolean expression format.
OPERATORS = ["&", "|", "^"]
NEGATION = "~"
BOOLEANS = [True, False]


class ExprGenerator:
    # generate random operators.
    def genOpers(self, n):
        opers = [choice(OPERATORS) for _ in range(n)]
        return opers

    # generate random variables with dense id.
    def genVars(self, n):
        id = [randint(0, n) for _ in range(0, n+1)]
        rank = list(set(id))
        ranked_id = [rank.index(i) for i in id]
        vars = ['v{0}'.format(i) for i in ranked_id]
        return vars

    # generate random negation.
    def genNegation(self, n):
        negation = [choice(BOOLEANS) for _ in range(n+1)]
        return negation

    # generate random expr.
    def genExpr(self, n):
        self.opers = self.genOpers(n)
        self.vars = self.genVars(n)
        self.neg = self.genNegation(n)
        self.expr = self._convert(self.opers, self.vars, self.neg, n)
        return self.expr

    # convert all to expr(string).
    def _convert(self, opers, vars, neg, n):
        expr = []
        for i in range(n):
            if neg[i] == True:
                expr.append(NEGATION)
            expr.append(vars[i])
            expr.append(opers[i])

        if neg[-1] == True:
            expr.append(NEGATION)
        expr.append(vars[-1])
        expr = ' '.join(expr)
        return expr
