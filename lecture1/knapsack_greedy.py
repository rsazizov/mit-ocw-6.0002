#!/usr/bin/env python3

class Item:
  def __init__(self, name, value, weight):
    self.name = name
    self.value = value
    self.weight = weight

  def get_value(self):
    return self.value

  def get_weight(self):
    return self.weight
  
  def get_density(self):
    return self.value / self.weight

  def __str__(self):
    return f'{self.name}: <{self.value}, {self.weight}>'

def build_items(names, values, weights):
  items = []
  
  for name, value, weight in zip(names, values, weights):
    items.append(Item(name, value, weight))

  return items

def greedy(items, max_weight, key):
  sorted_items = sorted(items, key=key, reverse=True)

  value = 0
  weight = 0
  result = []

  for item in sorted_items:
    if item.weight + weight <= max_weight:
      result.append(item)
      value += item.value
      weight += item.weight

  return result, value

def test_greedy(items, max_weight, key, key_name):
  print(f'Greedy, key = {key_name}')
  result, value = greedy(items, max_weight, key)

  for item in result:
    print(item)

  print('---')
  print(f'Value: {value}')
  print()

def greedys():
  names = ['clock','painting','radio','vase','book','computer']
  values = [175,90,20,50,10,200]
  weights = [10,9,4,2,1,20]
  max_weight = 20

  items = build_items(names, values, weights)

  test_greedy(items, max_weight, lambda x: 1 / Item.get_value(x), 'value')
  test_greedy(items, max_weight, Item.get_weight, 'weight')
  test_greedy(items, max_weight, Item.get_density, 'density')


greedys()
