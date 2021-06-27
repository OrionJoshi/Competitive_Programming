# Method-4 : Using Stack

def reverseList(arr):

  # creata a empty stack
  stack = []
  reversedArray = []

  # inserting elements in a stack
  for x in arr:
    stack.append(x)

  # removing elements from stack and insert in reversedArray list
  for i in range(len(stack)):
    reversedArray.append(stack.pop())

  return reversedArray

print(reverseList([1,2,3,4,5]))


# Time Complexity : O(n)
# Space Complexity : O(n)

  