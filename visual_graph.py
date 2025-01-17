import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
from population_simulation import *
from mayavi import mlab


def flat_graph_net(population, infection):
	graph = nx.DiGraph(population)
	fig = plt.figure()
	pos = nx.spring_layout(graph)
	nx.draw_networkx_nodes(graph,pos, node_size = 20, nodelist = infection[0], node_color = 'xkcd:red', with_labels = True)
	nx.draw_networkx_nodes(graph,pos, node_size = 10, nodelist = infection[1], node_color = 'xkcd:green', with_labels = True)
	nx.draw_networkx_edges(graph,pos, edge_list = nx.to_edgelist(graph),edge_color = 'w', arrows = False)
	fig.set_facecolor('xkcd:black')
	plt.axis('off')
	plt.show()


def d3_graph_net(population, probability):
	print(population)
	mlab.options.offscreen = False
	graph = nx.DiGraph(population)
	fig = plt.figure()
	pos = nx.random_layout(graph, dim=3)
	#pos = nx.spring_layout(graph, dim=3, k=50)
	xyz = np.array([pos[v] for v in sorted(graph)])
	#scalars = np.zeros(len(population))
	scalars = binary_vect(population, probability)

	print(scalars)
	mlab.figure(1, bgcolor=(0, 0, 0))
	mlab.clf()
	pts = mlab.points3d(xyz[:, 0], xyz[:, 1], xyz[:, 2],
	                    scalars,
	                    scale_factor=0.025,
	                    scale_mode='none',
	                    colormap='blue-red',
	                    resolution=50)

	pts.mlab_source.dataset.lines = np.array(list(graph.edges()))
	tube = mlab.pipeline.tube(pts, tube_radius=0.005)
	mlab.pipeline.surface(tube, color=(1, 1, 1), opacity = .05)

	mlab.show()

d3_graph_net(adjacent_mat(adjacent_list(50000,23)), .95)
