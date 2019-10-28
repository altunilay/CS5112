# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

# An implementation of a weighted, directed graph as an edge list. This means
# that it's represented as a list of tuples, with each tuple representing an
# edge in the graph.
class Graph:
  def __init__(self):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.graph = []

  def add_edge(self, node1, node2, weight):
    # Adds a directed edge from `node1` to `node2` to the graph with weight
    # defined by `weight`.

    # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code    
    raise NotImplementedError

  def has_edge(self, node1, node2):
    # Returns whether the graph contains an edge from `node1` to `node2`.
    # DO NOT EDIT THIS METHOD
    return (node1, node2) in [(x,y) for (x,y,z) in self.graph]

  def get_neighbors(self, node):
    # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    # `x` is the neighbor node, and `y` is the weight of the edge from `node`
    # to `x`.

    # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code
    raise NotImplementedError
