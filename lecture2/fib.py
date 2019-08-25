#!/usr/bin/env python3
import time

def fib(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  return fib(n - 1) + fib(n - 2)

def fib_dp(n, memo={}):
  if n == 0:
    return 0

  if n == 1:
    return 1

  if n in memo:
    return memo[n]
  else:
    memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]

t = time.perf_counter()
n = int(input('n = '))

print(fib(n))
print('Time:', time.perf_counter() - t)

t = time.perf_counter()

print(fib_dp(n))
print('Time:', time.perf_counter() - t)

