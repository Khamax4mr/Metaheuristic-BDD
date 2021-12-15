# random boolean expression generator.
from random import randint, choice

# this system follows dd's boolean expression format.
AND, OR, XOR, NOT = "&", "|", "^", "~"
OPERATORS = [AND, OR, XOR]
NEGATION = NOT
BOOLEANS = [True, False]


class ExprGenerator:

    # generate random expr.
    def genExpr(self, n):
        self.opers = self._genOpers(n)
        self.vars = self._genVars(n+1)
        self.negs = self._genNegs(n+1)
        self.expr = self._convert(self.opers, self.vars, self.negs, n)
        return self.expr

    # generate random binary operators.
    def _genOpers(self, n):
        opers = [choice(OPERATORS) for _ in range(n)]
        return opers

    # generate random variables with dense id.
    def _genVars(self, n):
        id = [randint(0, n) for _ in range(0, n)]
        rank = list(set(id))
        ranked_id = [rank.index(i) for i in id]
        vars = ['v%d' % i for i in ranked_id]
        return vars

    # generate random unary operators.
    def _genNegs(self, n):
        negation = [choice(BOOLEANS) for _ in range(n)]
        return negation

    # convert all to expr string format.
    def _convert(self, opers, vars, negs, n):
        exprList = []
        i = 0
        for i in range(n):
            if negs[i] == True:
                exprList.append(NEGATION)
            exprList.append(vars[i])
            exprList.append(opers[i])

        if negs[-1] == True:
            exprList.append(NEGATION)
        exprList.append(vars[-1])
        expr = ' '.join(exprList)
        return expr
