# Metaheuristic model checking

## Goal
We use metaheuristic in model checking to find counterexample which violates property in efficient way and to deal the state space explosion problem.

- [ ] Generate model structure.
- [ ] Apply metaheuristic algorithm.
- [ ] Search model checking examples.


## Function design

* **Initialisation**
Create transition list Individual with transition Element. Each individual has a different size, but the maximum is limited to a specified value.

* **Stopping criteria**
If no evolution for certain times, then stop the progress.

* **Fitness**
Except Individual with infeasible transition. (model checking results have boolean value, so need to find better way!)

* **Selection**
Select parents by the algorithm that can select variety samples like Stochastic.

* **Crossover**
Create new Individuals from selected parents by crossing transition list with same state. Be sure no exceed maximum size.

* **Mutation**
Create new Individuals by mutating transition list as feasible form.