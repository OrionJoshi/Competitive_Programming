# Method-1 Binary Search

def nextGreatestLetter(self, letters, target):
  l = 0
  r = len(letters) - 1
  while l <= r:
     mid = (l + r)//2
     if letters[mid] > target:
        r = mid -1
     else:
        l = mid + 1
  return letters[l % len(letters)]

# Time Complexity : O(logn)
# Space Complexity : O(1)