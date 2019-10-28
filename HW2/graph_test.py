# This is a short test file, given to you to ensure that our grading scripts can grade your file.
# Please do not modify it.
# You should only submit "graph_adjacency_list.py", "graph_edge_list.py", and "shortest_path.py".

# This tests the simplest case: adding a single edge to the graph and then checking whether has_edge
# confirms the edge's existance and that get_neighbors on the first node returns the second node.

from graph_adjacency_list import Graph as AdjacencyGraph
from graph_edge_list import Graph as EdgeGraph
import sys

try:
  print("Testing adjacency list graph...")
  adjacency_graph = AdjacencyGraph()
  adjacency_graph.add_edge('a', 'b', 1)
  if not adjacency_graph.has_edge('a', 'b'):
    print "Your code ran, but did NOT give True when checking whether the graph has an edge ('a', 'b') after adding edge ('a', 'b', 1)."
  else:
    print "Your code ran, and it correctly output True when checking whether the graph has an edge ('a', 'b') after adding edge ('a', 'b', 1)."
except:
  print "Your code produced this error when adding edge ('a', 'b', 1) or checking has_edge('a', 'b')."
  print sys.exc_info()[0]
try:
  if adjacency_graph.get_neighbors('a') != [('b', 1)]:
    print "Your code ran, but did NOT output the right neighbors for 'a' when adding edge ('a', 'b', 1)."
  else:
    print "Your code ran, and it correctly output the right neighbors for 'a' when adding edge ('a', 'b', 1)."
except:
  print "Your code produced this error when adding edge ('a', 'b', 1) or getting neighbors for 'a'."
  print sys.exc_info()[0]

try:
  print("Testing edge list graph...")
  edge_graph = EdgeGraph()
  edge_graph.add_edge('a', 'b', 1) 
  if not edge_graph.has_edge('a', 'b'):
    print "Your code ran, but did NOT give True when checking whether the graph has an edge ('a', 'b') after adding edge ('a', 'b', 1)."
  else:
    print "Your code ran, and it correctly output True when checking whether the graph has an edge ('a', 'b') after adding edge ('a', 'b', 1)."
except:
  print "Your code produced this error when adding edge ('a', 'b', 1) or checking has_edge('a', 'b')."
  print sys.exc_info()[0]
try:
  if edge_graph.get_neighbors('a') != [('b', 1)]:
    print "Your code ran, but did NOT output the right neighbors for 'a' when adding edge ('a', 'b', 1)."
  else:
    print "Your code ran, and it correctly output the right neighbors for 'a' when adding edge ('a', 'b', 1)."
except:
  print "Your code produced this error when adding edge ('a', 'b', 1) or getting neighbors for 'a'."
  print sys.exc_info()[0]
