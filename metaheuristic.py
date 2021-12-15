from dd.autoref import BDD

import config

from random import shuffle, choices, randint
from copy import copy
from functools import partial
from sys import maxsize

KEY, FIT = 0, 1


# new individual. the sequence of ordering.
def createIndividual(n):
    ind = [i for i in range(0, n)]
    shuffle(ind)
    return ind

# new population.
def createPopulation(nVar, psize):
    pop = [createIndividual(nVar) for _ in range(psize)]
    return pop

# check the number of nodes.
def evaluate(bdd, vars, nVar, ind):
    ordering = {}
    for i in range(nVar):
        ordering[vars[i]] = ind[i]
    BDD.reorder(bdd, ordering)
    score = len(bdd)
    return score


# crossover. FPS selection.
def crossover(nVar, popChain):
    pop = [key for key, _ in popChain]
    newPop = []
    
    # select weight.
    weight = fps_basic(popChain)

    for _ in range(config.POOL_SIZE):
        # select parents.
        parents = choices(popChain, weight, k=2)
        aParent = parents[0][KEY]
        bParent = parents[1][KEY]

        # get offsprings.
        pivot = randint(0, nVar)
        aParts = aParent[0:pivot]
        bParts = bParent[0:pivot]
        shuffle(aParts)
        shuffle(bParts)
        aOffspring = aParts + aParent[pivot:]
        bOffspring = bParts + bParent[pivot:]

        # insert identical element.
        if aOffspring not in pop:
            newPop.append(aOffspring)
        if bOffspring not in pop:
            newPop.append(bOffspring)
            
    newChain = [chain(ind) for ind in newPop]
    return newChain

# run FPS, weight from fitness.
def fps_basic(popChain):
    weight = [f for _, f in popChain]
    return weight

# new population (chain) with small change.
def mutation(popChain):
    newPop = [key for key, _ in popChain]
    for ind in newPop:
        loc1, loc2 = choices(ind, k=2)
        ind[loc1], ind[loc2] = ind[loc2], ind[loc1]
    newChain = [chain(ind) for ind in newPop]
    return newChain


def run(expr, vars):
    # BDD initialization.
    bdd = BDD()
    bdd.declare(*vars)
    bdd.add_expr(expr)
    nVar = len(vars)

    if config.DEBUG == True:
        print("Target expr:", expr)

    # set functions.
    global chain
    chain = lambda x: (x, eval_with(x))
    get_eval = lambda x: x[FIT]
    eval_with = partial(evaluate, bdd, vars, nVar)

    # metaheuristic initialization.
    pop = createPopulation(nVar, config.POP_SIZE)
    popChain = [chain(ind) for ind in pop]
    lastScore = bestScore = maxsize
    satisfied = False
    nIter = 0

    while not satisfied:
        # evaluation.
        popChain.sort(key=get_eval)
        popChain = popChain[:config.POP_SIZE]
        bestInd, bestScore = popChain[0]

        # print better score.
        if lastScore > bestScore:
            lastScore = bestScore
            nIter = 0

            if config.DEBUG == True:
                print("Best Ind  :", bestInd)
                print("Best Score:", bestScore)
                print("Limitation:", nIter)
                print("========================================")

        newChain = crossover(nVar, popChain)
        newChain = mutation(newChain)
        if len(newChain) < config.CRITERIA:
            nIter += 1
            if nIter == config.N_LIMIT:
                break
        popChain.extend(newChain)

    if config.DEBUG == True:
        print("Best Ind  :", bestInd)
        print("Best Score:", bestScore)

    ordering = [0 for _ in range(nVar)]
    for i in range(nVar):
        ordering[bestInd[i]] = vars[i]
    return ordering