# Method-2 Iterative Method
def firstUniqueCharacter(str):
  for i in range(len(str)):
    isFound = True
    for j in range(len(str)):
      if i == j:
        continue
      if str[i] == str[j]:
        isFound = False
        break
    if(isFound):
      return i
  return -1

# Time Complexity : O(n^2)
# Space Complexity : O(1)