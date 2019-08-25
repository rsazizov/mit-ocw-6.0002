#!/usr/bin/env python3
import random
import time

class Item:
  def __init__(self, name, value, weight):
    self.name = name
    self.value = value
    self.weight = weight

  def get_name(self):
    return self.name

  def get_value(self):
    return self.value

  def get_weight(self):
    return self.weight

  def __str__(self):
    return f'{self.name}: <{self.value}, {self.weight}>'

def build_items(names, values, weights):
  items = []
  
  for name, value, weight in zip(names, values, weights):
    items.append(Item(name, value, weight))

  return items

def knapsack_search_tree(left_items, left_weight):
  if len(left_items) == 0 or left_weight == 0:
    result = (0, ())

  # We can't take the item. Explore the right branch.
  elif left_items[0].get_weight() > left_weight:
    result = knapsack_search_tree(left_items[1:], left_weight)

  # Explore both branches.
  else:
    # Take the item.
    taken = left_items[0]
    with_val, with_items = knapsack_search_tree(left_items[1:],
        left_weight - taken.get_weight())

    with_val += taken.get_value()

    # Don't take the item.
    without_val, without_items = knapsack_search_tree(left_items[1:],
        left_weight)

    if with_val > without_val:
      result = (with_val, with_items + (taken,))
    else:
      result = (without_val, without_items)

  return result

def knapsack_search_tree_dp(left_items, left_weight, memo={}):
  memo_key = (len(left_items), left_weight)
  if memo_key in memo:
    return memo[memo_key]
  if len(left_items) == 0 or left_weight == 0:
    result = (0, ())

  # We can't take the item. Explore the right branch.
  elif left_items[0].get_weight() > left_weight:
    result = knapsack_search_tree(left_items[1:], left_weight)

  # Explore both branches.
  else:
    # Take the item.
    taken = left_items[0]
    with_val, with_items = knapsack_search_tree_dp(left_items[1:],
        left_weight - taken.get_weight(), memo)

    with_val += taken.get_value()

    # Don't take the item.
    without_val, without_items = knapsack_search_tree_dp(left_items[1:],
        left_weight, memo)

    if with_val > without_val:
      result = (with_val, with_items + (taken,))
    else:
      result = (without_val, without_items)

  memo[memo_key] = result
  return result

def build_rand_items(n, max_val, max_weight):
  items = []

  for i in range(n):
    val = random.randint(1, max_val)
    weight = random.randint(1, max_weight)

    items.append(Item(str(i), val, weight))

  return items

def test(items, n, fn):
  max_weight = 40

  val, items = fn(items, max_weight)

  print('Taken items:')

  for item in items:
    print(item)

  print('-----')
  print('Total value:', val)

n = 35
items = build_rand_items(n, 10, 10)

t = time.perf_counter()
print('Search tree')
test(items, n, knapsack_search_tree)
print('Time:', time.perf_counter() - t)

t = time.perf_counter()

print('Search tree (dp)')
test(items, n, knapsack_search_tree_dp)
print('Time:', time.perf_counter() - t)

