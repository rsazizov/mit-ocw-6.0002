import random

random.seed(42)

def roll_die():
  return random.choice(range(1, 6 + 1))

def run_sim(goal, n):
  total = 0

  for _ in range(n):
    result = ''

    for _ in range(len(goal)):
      result += str(roll_die())
      
    if result == goal:
      total += 1

  return total / n

print('Estimated prob: ', run_sim('11111', 1000000))
