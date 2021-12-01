# Metaheuristic Binary Decision Diagram

## Binary Decision Diagram

![img1](./img/sample.png)

A [binary decision diagram (BDD)](https://en.wikipedia.org/wiki/Binary_decision_diagram) is directed acyclic graph to represent a boolean function. BDD is useful implementational framework for some computational problems and symbolic model-checking.

First, consider the simpler form, *binary decision tree* ***(Fig 1)***. It is a tree whose non-terminal nodes are labelled with boolean variables and terminal nodes are labelled with either 0 or 1. Each non-terminal node has two edges which represent an assignment of the value 0 or 1 to its boolean variable.

BDD can be optimised into more compact form, *reduced*, ordered BDD (ROBDD) ***(Fig 2)***. BDD almost always refers to ROBDD. ROBDD is canonical (unique) for certain veriable order. This is desirable property for formal equivalence checking.


## Variable Ordering Problem

![img2](./img/ordering.png)

The size of the BDD is determined by boolean function and ordering of the variables. It is important to choose good variable ordering when applying BDD. It makes a significant difference to the size of BDD. See ***Fig 3*** and ***Fig 4***. Both are BDDs with same boolean function but different ordering. However ***Fig 4*** is much simple than ***Fig 3***.

The problem of finding the best variable ordering is **NP-hard**.


## Goal

* Find best BDD ordering on efficient way by metaheuristic solution.
* Apply this system to BDD-based model-checking.
