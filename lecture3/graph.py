from typing import List

class Node:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def get_name(self):
    return self.name

class Edge:
  def __init__(self, src, dst):
    self.src = src
    self.dst = dst

  def __str__(self):
    return self.src.get_name() + '->' + self.dst.get_name()

  def get_src(self):
    return self.src

  def get_dst(self):
    return self.dst

class Digraph:
  def __init__(self):
    self.edges = {}

  def __str__(self):
    s = ''

    for src in self.edges:
      for dst in self.edges[src]:
        s = s + src.get_name() + '->' + dst.get_name() + '\n'

    return s[:-1]

  def has_node(self, node):
    if type(node) == str:
      try:
        self.get_node(node)
        return True
      except NameError:
        return False
    elif type(node) == Node:
      return node in self.edges

  def add_node(self, node):
    if self.has_node(node):
      raise NameError(f'Node {node.get_name()} already exists')

    self.edges[node] = []

  def get_node(self, name):
    for node in self.edges:
      if node.get_name() == name:
        return node

    raise NameError('Node not found')

  def add_edge(self, edge):
    if not self.has_node(edge.src) or not self.has_node(edge.dst):
      raise ValueError('Source or destination node is not in the graph')
    
    self.edges[edge.src].append(edge.dst)

  def children_of(self, node):
    if type(node) == str:
      return self.edges[self.get_node(node)]
    elif type(node) == Node:
      return self.edges[node]
    else:
      raise TypeError('str or Node expected')

class Graph(Digraph):
  def add_edge(self, edge):
    Digraph.add_edge(self, edge)
    rev_edge = Edge(edge.dst, edge.src)
    Digraph.add_edge(self, rev_edge)

def build_city_graph(graph_type):
  g = graph_type()

  for name in ('Boston', 'Providence', 'New York', 'Chicago',
    'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
    g.add_node(Node(name))

  g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
  g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
  g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
  g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
  g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
  g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
  g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
  g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
  g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
  g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
  
  return g

def path_to_str(path: List[Node]):
  if path is None or path == []:
    return ''

  return '->'.join(map(Node.get_name, path))

