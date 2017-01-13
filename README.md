Problem Generators
==================

This repository contains some scripts to create LP-files for randomly generated
multi-objective integer programming problems. Note the peculiar format of these
files, the objective (as defined by the LP file format) is 0, the multiple
objectives are all given as constraints. The last "x" constraints will have
right-hand-side values of 1,2,3,...,x, where x is the number of objectives for
your problem.

Currently, the only known (to the author) solver which handles such files is
[moip_aira](http://github.com/WPettersson/moip_aira).


Assignment Problems
-------------------

Usage: ./generate_AP.py <lpfile> <num-tasks> <num-objectives>

where lpfile is the name of the file you wish to create, num-tasks is the
number of tasks (equivalently number of workers) in the problem and
num-objectives is the number of objectives you wish to minimise.

Example: ./generate_AP.py 5AP-50.lp 50 5

This will create an assignment problem with 50 tasks, 50 workers, and 5
objective functions.

Knapsack Problems
-----------------

Usage: ./generate_KP.py <lpfile> <num-vars> <num-objectives>

where lpfile is the name of the file you wish to create, num-vars is the number
of variables in the knapsack problem, and num-objectives is the number of
objectives you wish to maximise.

Example: ./generate_KP.py KD4D-100.lp 100 4

This will create a knapsack problem with 100 variables and 4 objective
functions.
