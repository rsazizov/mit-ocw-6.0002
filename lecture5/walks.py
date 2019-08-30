import random

class Location:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f'<{self.x}, {self.y}>'

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

  def dist_from(self, other):
    x_dist = self.x - other.get_x()
    y_dist = self.y - other.get_y()

    return (x_dist ** 2 + y_dist ** 2) ** 0.5;

  def move(self, dx, dy):
    return Location(self.x + dx, self.y + dy)

class Drunk:
  def __init__(self, name=None):
    self.name = name

  def __str__(self):
    return self.name or 'Anonymous'

class UsualDrunk(Drunk):

  def take_step(self):
    step_choices = [(0,1), (0, -1), (1, 0), (-1, 0)]
    return random.choice(step_choices)

class MasochistDrunk(Drunk):

  def take_step(self):
    step_choices = [(0,1.1), (0, -0.9), (1.0, 0), (-1.0, 0)]
    return random.choice(step_choices)

class ColdDrunk(Drunk):

  def take_step(self):
    step_choices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0), (-1.0, 0.0)]
    return random.choice(step_choices)

class EWDrunk(Drunk):

  def take_step(self):
    step_choices = [(1, 0), ( -1, 0)]
    return random.choice(step_choices)

class Field:
  def __init__(self):
    self.drunks = {}

  def add_drunk(self, drunk, loc):
    if drunk in self.drunks:
      raise ValueError('Duplicate drunk')

    self.drunks[drunk] = loc

  def move_drunk(self, drunk):
    if drunk not in self.drunks:
      raise ValueError('Drunk is not in the field')

    x_dist, y_dist = drunk.take_step()

    self.drunks[drunk] = self.drunks[drunk].move(x_dist, y_dist)

  def get_loc(self, drunk):
    if drunk not in self.drunks:
      raise ValueError('Drunk not in the field')

    return self.drunks[drunk]

def walk(f: Field, d: Drunk, n_steps):
  start = f.get_loc(d)

  for _ in range(n_steps):
    f.move_drunk(d)

  return f.get_loc(d).dist_from(start)

def sim_walks(n_steps, n_trials, d_class):
  distances = [0] * n_trials

  for i in range(n_trials):
    f = Field()
    d = d_class()
    f.add_drunk(d, Location(0, 0))

    distances[i] = round(walk(f, d, n_steps), 1)

  return distances

def sim_drunk(n_trials, d_class, lengths):
  mean_distances = []

  for l in lengths:
    trials = sim_walks(l, n_trials, d_class)
    mean_distances.append(sum(trials) / n_trials)

  return mean_distances
