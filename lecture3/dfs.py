from graph import *

# Depth-First Search
def dfs(graph, start, end, to_print=True, path=[], shortest=None):
  
  # Since lists are passed by reference
  path = path + [start]

  # Meaningless to continue the search if the current path
  # is longer than the shortest.
  if shortest is not None and len(path) > len(shortest):
    return shortest

  if to_print:
    print(path_to_str(path))

  if end == start:
    return path

  for child in graph.children_of(start):
    # Avoid cyclces
    if child in path:
      continue

    new_path = dfs(graph, child, end, to_print, path, shortest)
    shortest = new_path or shortest

  return shortest


g = build_city_graph(Digraph)

print('Looking for the shortest path using DFS')
shortest = dfs(g, g.get_node('Boston'), g.get_node('Phoenix'))

print('---')
print('Shortest:', path_to_str(shortest))
