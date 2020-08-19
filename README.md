# Guide for the 380CT Assignment on TSP

The actual part you need to submit is the **Metaheuristics** section.
The rest is meant to introduce you to the basics.

## Lab 5

- Ensure you have Jupyter, and load `Investigating TSP.ipynb`.
	- Either launch `Anaconda` through [AppsAnywhere](https://appsanywhere.coventry.ac.uk), or if you are working on your machine then I recommend installing [Anaconda](https://www.anaconda.com/distribution).
- Familiarise yourself with Jupyter functionaility. Consider taking **LinkedIn Learning courses** (free through the university) or any suitable alternatives. Here is a recommended set (e.g. each member of the group takes one):

	- [Introducing Jupyter](https://www.linkedin.com/learning/introducing-jupyter/present-data-like-a-pro-with-jupyter)
	- [Get Ready for Your Coding Interview](https://www.linkedin.com/learning/get-ready-for-your-coding-interview/welcome)
	- [Python for Data Visualization](https://www.linkedin.com/learning/python-for-data-visualization/setting-marker-type-and-colors)
	- [Python: Programming Efficiently](https://www.linkedin.com/learning/python-programming-efficiently/time-profiling)
	- [Python Statistics Essential Training](https://www.linkedin.com/learning/python-statistics-essential-training/the-power-of-visualization)

- Study `Investigating TSP.ipynb`.
	- Can you improve any of the functions implemented in `Investigating TSP.ipynb` to make them mor efficient?
	- See how large you can make $n$ while testing `exhaustive_search()`.
	- Check that `greedy_nearest_neighbours()` is correct. If not then fix it!

- Read the [Wikipedia article on TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem). Pay attention to th **Computing a solution** section, and especially to the `2-opt` and `3-opt` techniques for defininf neighbourhoods.

- Experiment with generating your own graph families. For example:
	- **Euclidean graphs**: generate points using _(x,y)_ coordinates, then generate the adjacency matrix by calculating all the required distances. Recall that the distance between two points _(x<sub>1</sub>,y<sub>1</sub>)_ and _(x<sub>2</sub>,y<sub>2</sub>)_ is _sqrt[(x<sub>1</sub>-x<sub>2</sub>)<sup>2</sup>+(y<sub>1</sub>-y<sub>2</sub>)<sup>2</sup>]_.
	- **Graphs with obvious shortest cycle**: think of a graph where all the distances are 2 except for the edges on a predefined cycle, where the distance is 1. Such a graph would be useful for testing/debugging the *nearest neighbours greedy search*.
