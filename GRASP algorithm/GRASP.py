from random import sample, choice, shuffle, randint
from itertools import product, permutations
from pprint import pprint
from math import inf as oo
from math import sqrt
import math
from numpy import arange
from time import time
import copy
import matplotlib.pyplot as plt

MAX_DISTANCE = 100

def random_symetric_graph(n):
	''' Symetric adjacency matrix of size nxn '''
	dist_matrix = [[oo for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(i+1,n):
			v = randint(1, MAX_DISTANCE)
			dist_matrix[i][j] = v
			dist_matrix[j][i] = v
	return dist_matrix

def random_euclidean_graph(n):
	''' Symmetric adjacency matrix of a Euclidean graph of size nxn '''
	dist_matrix = [[oo for _ in range(n)] for _ in range(n)]
	points = []
	for p in range(n):
		x, y = randint(0, MAX_DISTANCE), randint(0, MAX_DISTANCE)
		points.append((x,y))
	for i in range(n):
		p1 = points[i]
		for j in range(i+1,n):
			p2 = points[j]
			distance = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
			dist_matrix[i][j] = distance
			dist_matrix[j][i] = distance
	return dist_matrix

def show(G):
	''' Show adjacency matrix. Useful for debugging. '''
	n = len(G)
	r = "  "
	for i in range(n):
		r += f' {i:4}'
	r += '\n    -' + '-' *(4*n)+ '\n'
	for i in range(n):
		r += f'{i:2} | '
		for j in range(n):
			r += f'{G[i][j]:4}'
		r += '\n'
	print(r)

def cost(G, cycle):
	'''Calculate the cost of the given cycle '''
	c = 0
	n = len(G)
	for i in range(n):
		a = cycle[i]
		b = cycle[(i+1)%n]
		c += G[a][b]
	return c

def greedy_rand_search(G):
	H = copy.deepcopy(G)
	n = len(H)
	cities = list(range(n))
	cycle = []
	newlist = []
	dist = 0
	nearest_city = 0
	city = 0
	while len(cities)>0:
		city_neighbours = H[city]
		count = 0
		random_distance = city_neighbours[randint(0, len(city_neighbours) - 1)]
		while math.isinf(random_distance):
			random_distance = city_neighbours[randint(0, len(city_neighbours) - 1)]
			if all_inf(city_neighbours):
				random_distance = oo
				break
		nearest_city = city_neighbours.index(random_distance)
		cycle.append(city)
		cities.remove(city)
		for i in range(n):
			H[city][i] = oo
			H[i][city] = oo
		if nearest_city != 0:
			city = nearest_city
	return (cycle, cost(G, cycle))

def all_inf(list):
	return all(x == list[0] for x in list)

G = random_symetric_graph(5)
show(G)
#greedy_rand_search(G)
print(greedy_rand_search(G))

for i in range(50):
	TE = random_symetric_graph(10)
	print(greedy_rand_search(G))