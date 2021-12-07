from generator import FormulaGenerator

from pyeda.inter import expr, bddvars
from pyeda.boolalg.bdd import expr2bdd, _NODES

from functools import partial
from random import randint, shuffle, choices
from sys import maxsize
from time import time

KEY, FIT = 0, 1
POP_SIZE = 500
POOL_SIZE = 50

# new individual.
def createIndividual(n):
    ind = [i for i in range(0, n)]
    shuffle(ind)
    return ind

# new population.
def createPopulation(nVar, psize):
    pop = [createIndividual(nVar) for _ in range(psize)]
    return pop

# check constraints limitation and sum.
def evaluate(bdd, nVar, ind):
    base = len(_NODES)
    node_map = {}
    for i in range(0, nVar):
        node_map[V[i]] = X[ind[i]]
    
    ind_bdd = bdd.compose(node_map)
    dst = len(_NODES)
    del ind_bdd

    return dst - base


# new population (chain) with small change.
def mutation(popChain):
    newPop = [popChain[i][KEY].copy() for i in range(POOL_SIZE)]
    for ind in newPop:
        loc1, loc2 = choices(ind, k=2)
        ind[loc1], ind[loc2] = ind[loc2], ind[loc1]
    newChain = [chain(ind) for ind in newPop]
    return newChain


def main():
    # initialize.
    pop = init_pop(POP_SIZE)
    popChain = [chain(ind) for ind in pop]

    lastScore = bestScore = maxsize
    startTime, endTime = time(), time()
    while (endTime-startTime) < 60:
        # evaluation.
        popChain.sort(key=get_eval)
        popChain = popChain[:POP_SIZE]
        bestInd, bestScore = popChain[0]
        endTime = time()

        # print better score.
        if lastScore > bestScore:
            lastScore = bestScore
            print("Time      :", endTime - startTime)
            print("Best Ind  :", bestInd)
            print("Best Score:", bestScore)
            print("========================================")

        newChain = mutation(popChain)
        popChain.extend(newChain)

    print("Message   :", "Time out.")
    print("Best Ind  :", bestInd)
    print("Best Score:", bestScore)


if __name__ == '__main__':
    # random formula generation.
    nOper = 10
    # target_bfunc = FormulaGenerator().genFormula(nOper)
    target_bfunc = "v[0]&v[1]|v[2]&v[3]|v[4]&v[5]|v[6]&v[7]|v[8]&v[9]|v[10]&v[11]"
    
    target_expr = expr(target_bfunc)
    target_bdd = expr2bdd(target_expr)
    nVar = len(target_expr.inputs)

    # set variables.
    global V, X
    V = bddvars('v', nVar)
    X = bddvars('x', nVar)

    # set functions.
    global init_pop, chain, get_eval, eval_with
    init_pop = partial(createPopulation, nVar)
    chain = lambda x: (x, eval_with(x))
    get_eval = lambda x: x[FIT]
    eval_with = partial(evaluate, target_bdd, nVar)

    print("Target func:", target_bfunc)
    print("========================================")
    main()
