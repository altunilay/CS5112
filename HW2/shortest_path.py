# TODO: Nilay Altun, na523
# TODO: Kelly Mayhew, khm53

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.

  # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code

  	visited_nodes = {}
  	visited_nodes[source] = ([source],0)

  	neighbours = graph.get_neighbors(source) or []

  	edge_options = []

  	for neighbor in neighbours:
  		edge_options.append((source,neighbor[0],neighbor[1]))

  	while edge_options:
  		edge_options = sorted(edge_options, key=lambda tup: tup[2])
  		smallest_edge = edge_options[0]
  		edge_options.pop(0)

  		smallest_node = smallest_edge[1]
		if smallest_node not in visited_nodes:
			new_path = list(visited_nodes[smallest_edge[0]][0])
			new_path.append(smallest_node)
			new_distance = visited_nodes[smallest_edge[0]][1] + smallest_edge[2]
			visited_nodes[smallest_node] = (new_path,new_distance)

			new_neighbours = graph.get_neighbors(smallest_node) or []

			for new_neighbor in new_neighbours:
				edge_options.append((smallest_node,new_neighbor[0], new_neighbor[1]))
				
		else:
			new_distance = visited_nodes[smallest_edge[0]][1] + smallest_edge[2]
			if new_distance < visited_nodes[smallest_node][1]:
				new_path = list(visited_nodes[smallest_edge[0]][0])
				new_path.append(smallest_node)
				visited_nodes[smallest_node] = (new_path,new_distance)


	return(visited_nodes[target])


