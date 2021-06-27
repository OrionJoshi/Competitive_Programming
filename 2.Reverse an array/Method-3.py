# Method-3 : Using Python Slice operator

def reverseArray(arr):
  # slicing
  return arr[::-1]

intArray = [1,2,3,4,5]

print("Before Reversing : ",intArray )

resultArray = reverseArray(intArray)

print("After Reversing : ",resultArray )

# Time Complexity : O(n)
# Space Complexity : O(1)

