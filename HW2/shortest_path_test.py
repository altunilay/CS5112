# This is a short test file, given to you to ensure that our grading scripts can grade your file.
# Please do not modify it.
# You should only submit "graph_adjacency_list.py", "graph_edge_list.py", and "shortest_path.py".

# This tests the simplest case: adding a single edge to the graph and checking the shortest path from one node to the other.

from graph_adjacency_list import Graph as AdjacencyGraph
from graph_edge_list import Graph as EdgeGraph
from shortest_path import shortest_path
import sys

try:
  print("Testing with adjacency list graph...")
  adjacency_graph = AdjacencyGraph()
  adjacency_graph.add_edge('a', 'b', 1)
  if shortest_path(adjacency_graph, 'a', 'b') != (['a','b'], 1):
    print "Your code ran, but did NOT output the shortest distance from 'a' to 'b' when your adjacency list graph had the edge ('a', 'b', 1) added."
  else:
    print "Your code ran, and it correctly output the shortest distance from 'a' to 'b' when your adjacency list graph had the edge ('a', 'b', 1) added."
except:
  print "Your code produced this error when adding edge ('a', 'b', 1) to the adjacency list graph or getting the shortest path from 'a' to 'b'."
  print sys.exc_info()[0]

try:
  print("Testing with edge list graph...")
  edge_graph = EdgeGraph()
  edge_graph.add_edge('a', 'b', 1) 
  if shortest_path(edge_graph, 'a', 'b') != (['a','b'], 1):
    print "Your code ran, but did NOT output the shortest distance from 'a' to 'b' when your edge list graph had the edge ('a', 'b', 1) added."
  else:
    print "Your code ran, and it correctly output the shortest distance from 'a' to 'b' when your edge list graph had the edge ('a', 'b', 1) added."
except:
  print "Your code produced this error when adding edge ('a', 'b', 1) to the edge list graph or getting the shortest path from 'a' to 'b'."
  print sys.exc_info()[0]
