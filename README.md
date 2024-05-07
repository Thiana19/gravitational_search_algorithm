# Knapsack Problem Solver using Gravitational Search Algorithm

## A- WHAT IS KNAPSACK PROBLEM?
The Knapsack Problem is a classic optimization problem in computer science and combinatorial optimization. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is maximized.
The knapsack problem can be modeled as the following where:

![Example Image](images/knapsack.png)

## B- WHAT IS GRAVITATIONAL SEARCH ALGORITHM?
Gravitational Search Algorithm is one of the various heuristic optimization methods that have
been developed recently. Unlike the others that are inspired by swarm behavior, the GSA is
based on the law of gravity and mass interactions. Basically, the agents are a collection of
masses that interact with each other based on the Newtonian gravity and laws of motion. In
the process these steps are required: initialization, calculate the gravitational forces,
calculate the acceleration and velocity, update the position of the solution.

## C- METHODOLOGY
Searching for research papers on application of GSA in solving the knapsack problem, we
found a few that were not very detailed in terms of the algorithm. So, we decided to use the
general algorithm for the GSA and try and adapt it to the knapsack problem ourselves. We
referred to Wei Lei’s algorithm structure as the basis for developing our algorithm. Since the
problem was of combinatorial optimization, we encoded the problem in binary. This meant
we needed to use a version of GSA that could work on binary encoded solution space. We
found Rashedi et al.’s paper on binary gravitational search algorithm that presented the
necessary changes required in GSA to make it work with binary encoded solution space. Only
the position function of GSA was modified to a probability based function that changed the
position bits to 0 or 1 based on the velocity of the agent. We modified our base to incorporate
this change and also used a hamiltonian distance in calculating the R in the force function
instead of the euclidean distance as in the traditional GSA. We also referred to Gupta’s work
on a hybrid GA-GSA algorithm to get a better understanding of the steps required in applying
GSA to the knapsack problem. The GSA algorithm consists of the following steps: initialization,
fitness value calculation, calculation of force, calculation of acceleration, velocity update and
position update.

### STEP 1: INITIALIZATION
To initialize the algorithm, a random population of solutions is created. The number of
solution N in a population is one of the parameters that can be modified in the algorithm to
yield different test results. The population in our employed algorithm is generated using a
5
loop with the given weight constraint of 65 that selects a random mutant every loop and adds
it to a list representing a solution. Along with the solution, a bitmap of the mutant list is also
updated and maintained. The bitmap has 0s and 1s in the form of a list, each corresponding
to a mutant. Whenever a mutant is selected, the corresponding bit for the mutant is updated
to 1 to denote that the mutant has been selected. The solution formed after the completion
of the loop is checked again to see if the last addition of mutant caused the total weight of
the solution to exceed the weight constraint. If it did, it is dropped from the list and the bitmap
for the corresponding mutant is also changed to 0. Finally, the solution is added to the list of
solutions, i.e., population and the bitmap to the list of bits. The whole process reiterates for
N times so that the population has N solutions after the end of the initialization step. Besides
this, the initialization step also includes the initialization of the velocity of each of the
solutions to 0. The initialization occurs only once per run.

### STEP 2: CALCULATION OF FITNESS VALUE AND MASS OF THE SOLUTIONS
Evaluate the fitness value of each solution based on its feasibility and objective function value. Calculate the mass of each solution.

### STEP 3: CALCULATION OF FORCE ON THE MASSES
Calculate the gravitational force acting on each solution based on its mass and the distance between solutions.

### STEP 4: CALCULATION OF ACCELERATION
Calculate the acceleration of each solution based on the gravitational force acting on it.

### STEP 5: UPDATING VELOCITY
Update the velocity of each solution based on its current velocity and acceleration.

### STEP 6: UPDATING POSITION
Update the position of each solution based on its current position and velocity.

## D- EVALUATION
In the evaluation section, we present the results of applying the Gravitational Search Algorithm to solve the Knapsack Problem. We provide the outcomes of two trial runs:

### Trial 1
Describe the setup and results of the first trial.

### Trial 2
Describe the setup and results of the second trial.

## E- CONCLUSION
In conclusion, the Gravitational Search Algorithm shows promise in solving the Knapsack Problem efficiently by leveraging the principles of gravity and motion. Further experimentation and optimization can potentially improve its performance and applicability in various real-world scenarios.

