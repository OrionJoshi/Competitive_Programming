# Method-2 

def validSubsequence(array, substring):
  substringIdx = 0

  for value in array:
    if substringIdx == len(substring):
      break
    if substring[substringIdx] == value:
      substringIdx += 1
  return substringIdx == len(substring)

# Time Complexity : O(n)
# Space Complexity : O(1)