# Method - 2 Iterative

def firstBadVersion(n):

  for i in range(1, n + 1):
      if isBadVersion(i):
          return i

# Time Complexity : O(n)
# Space Complexity : O(1)