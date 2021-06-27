# Method-1: Iterative method

def reverseArray(arr):
  startIndex = 0
  lastIndex = len(arr) - 1

  while startIndex < lastIndex:
    arr[startIndex], arr[lastIndex] = arr[lastIndex], arr[startIndex]
    startIndex += 1
    lastIndex -= 1

  return arr

print(reverseArray([1,2,3,4,5]))

# Time Complexity : O(n)
# Space Complexity : O(1)