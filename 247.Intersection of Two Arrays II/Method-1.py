# Method-1

from collections import Counter

def intersect(nums1, nums2):           
      c1 = Counter(nums1)
      c2 = Counter(nums2)
      result = []

      for key in c1 & c2:
          result += [key]*min(c1[key], c2[key])

      return result

# Time Complexity : O(n)
# Space Complexity : O(n)