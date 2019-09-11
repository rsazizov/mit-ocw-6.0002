# Pascal's problem
import random

def roll_die():
  return random.choice(range(1, 6 + 1))

def pascal(n_trials):
  n_wins = 0

  for _ in range(n_trials):
    for _ in range(24):
      d1 = roll_die()
      d2 = roll_die()

      if d1 == 6 and d2 == 6:
        n_wins += 1
        break

  return n_wins / n_trials

print('P of winning:', pascal(1000000))
