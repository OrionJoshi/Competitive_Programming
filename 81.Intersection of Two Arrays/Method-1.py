# Method-1 Iterative

def intersection(nums1, nums2):
    
    result = []
    
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)
            
    return result

# Time Complexity : O(n * m)
# Space Complexity : O(n or m)