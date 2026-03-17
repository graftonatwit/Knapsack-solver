# Knapsack-solver
KnapsackSolver
Overview

KnapsackSolver is a Python program that solves the classic 0-1 Knapsack problem using multiple approaches:

Dynamic Programming – guaranteed optimal solution.

Greedy Heuristic – fast, approximate solution.

Enumeration / Brute Force – checks all possible combinations (for small datasets).

The program reads items from a text file, where each line specifies an item’s weight and value, and finds the optimal subset of items that maximizes total value without exceeding the knapsack’s capacity.

Features

Dynamic Programming Solution

Uses a 2D DP table to find the optimal value.

Returns the selected items and total value.

Greedy Heuristic Solution

Sorts items by value-to-weight ratio and picks the best-fitting items.

Faster but may not always find the optimal solution.

Enumeration / Brute Force

Checks all combinations of items.

Guaranteed optimal but only feasible for small item sets (≤ 20 items).

Flexible Input

Items can be loaded from a file with simple weight-value pairs.

Input Format

The program expects a text file with one item per line in the following format:

weight price
weight price
weight price

Example (item.txt):

10 60
20 100
30 120

weight – integer weight of the item

price – integer value of the item

Usage

Clone the repository:

git clone <your-repo-url>
cd KnapsackSolver

Prepare the items file:

Create item.txt in the same folder, with weight and price for each item.

Run the solver:

python knapsack_solver.py

Output:

Displays the selected items and total price for each algorithm:

Dynamic Solution: price 220 items: [1, 2]
Greedy Solution: price 180 items: [2, 0]
Enumeration Solution: price 220 items: [1, 2]
Example

With capacity = 50 and items:

10 60
20 100
30 120

Dynamic Programming: Optimal value 220 → items [1, 2]

Greedy Heuristic: Approximate value 180 → items [2, 0]

Enumeration: Optimal value 220 → items [1, 2]

Code Structure

KnapsackSolver class:

read_items(filename) – read weight/value pairs from file

find_dynamic(items, capacity) – dynamic programming solution

find_greedy(items, capacity) – greedy heuristic solution

find_enumerate(items, capacity) – brute-force enumeration solution

Main block:

Reads items

Solves with each method

Prints results

Requirements

Python 3.6+

No external libraries needed

Notes

Dynamic Programming: Optimal but may use more memory for large capacities.

Greedy Heuristic: Fast, suitable for large datasets, but may be suboptimal.

Enumeration: Only feasible for ≤ 20 items because of exponential time complexity.

Author

Trevor Grafton

Implemented a multi-approach solution for the 0-1 Knapsack problem
