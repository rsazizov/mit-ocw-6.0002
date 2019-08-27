from graph import *

def bfs(graph, start, end, to_print=True):
  path_queue = [[start]]

  while len(path_queue) > 0:
    path = path_queue.pop(0)
    node = path[-1]

    if to_print:
      print(path_to_str(path))

    if node == end:
      return path

    for child in graph.children_of(node):
      if child in path:
        continue

      new_path = path + [child]
      path_queue.append(new_path)

  return None

g = build_city_graph(Digraph)

print('Looking for the shortest path using BFS')
shortest = bfs(g, g.get_node('Boston'), g.get_node('Phoenix'))

print('---')
print('Shortest:', path_to_str(shortest))
