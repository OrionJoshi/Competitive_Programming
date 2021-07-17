# Method-2 Iterative

def lenOfLastWord(str):
  count = 0
  for x in reversed(str):
      if x == ' ':
          return count
      else:
          count += 1
  return count

# Time Complexity : O(n)
# Space Complexity : O(1)


