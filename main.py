import numpy as np
import math
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
from population_simulation import *
from mayavi import mlab

if __name__ == '__main__':

    print('What population size do you want?')
    population_size = int(input())
    print('What number of encounters do you want?')
    possible_ecnounters = int(input())
    print('Simulation Population')
    population = adjacent_list(population_size, possible_ecnounters)
    population_mat = adjacent_mat(population)
