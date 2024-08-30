import sys
sys.setrecursionlimit(5000)

def recursive_function(n, sum):
  if n < 1:
      return sum
  else:
      return recursive_function(n - 1, sum + n)

print(recursive_function(1000, 0))