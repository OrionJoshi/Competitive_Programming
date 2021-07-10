# Method-1 Iterative Method
def threeLargestNumbers(array):
  threeLargest = [None, None, None]
  for num in array:
    updateLargest(threeLargest, num)
  return threeLargest

# helper functions
def updateLargest(threeLargest, num):
  if threeLargest[2] is None or num > threeLargest[2]:
    shiftAndUpdate(threeLargest, num, 2)
  elif threeLargest[1] is None or num > threeLargest[1]:
    shiftAndUpdate(threeLargest, num, 1)
  elif threeLargest[0] is None or num > threeLargest[0]:
    shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
  for i in range(idx + 1):
    if i == idx:
      array[i] = num
    else:
      array[i] = array[i + 1]

# Time Complexity : O(n)
# Space Complexity : O(1)