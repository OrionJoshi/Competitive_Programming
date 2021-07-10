# Method-2 By Sorting
def threeLargestNumbers(array):
  resultArray = []
  length = len(array)
  array.sort()
  for x in range(length - 3, length):
      resultArray.append(array[x])
  return resultArray
  
threeLargestNumbers([11,72,2,3,4,5])

# Time Complexity : O(nlogn) Assuming use of 
#                                best sorting algorithm
# Space Complexiy : O(1)