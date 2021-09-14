# Method-2 Using List comprehension

def intersection(nums1, nums2):
    
    return list(set([num for num in nums1 if num in nums2 ]))

# Time Complexity : O(n * m)
# Space Complexity : O(n or m)