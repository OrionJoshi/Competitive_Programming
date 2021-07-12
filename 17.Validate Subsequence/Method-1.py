# Method-1 Using while loop

def validSubsequence(array, substring):
  subStringIdx = 0
  arrayIdx = 0

  while arrayIdx < len(array) and subStringIdx < len(substring):
    if substring[subStringIdx] == array[arrayIdx]:
      subStringIdx += 1
    arrayIdx += 1
  return subStringIdx == len(substring)

# Time Complexity : O(n)
# Space Complexity : O(1)