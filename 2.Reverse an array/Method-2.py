# Method-2 : Recursive Method

def reverseArray(arr, start, end):
  if start > end:
    return
  arr[start], arr[end] = arr[end], arr[start]
  reverseArray(arr, start + 1, end - 1)


intList = [1,2,3,4,5]
arrayLenght = len(intList)

print("Before Reversing : ",intList )

reverseArray(intList, 0, arrayLenght - 1)

print("After Reversing : ",intList )

# Time Complexity : O(n)
# Space Complexity : O(n)


