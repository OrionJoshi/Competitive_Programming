# Method-1

def chalkReplacer(chalk, k):
  k %= sum(chalk)
  if k == 0:
    return 0

  for i, c in enumerate(chalk):
    k -= c
    if k < 0:
      return i

# Time Complexity : O(n)
# Space Complexity : O(1)