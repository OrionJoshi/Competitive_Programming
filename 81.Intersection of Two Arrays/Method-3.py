# Method-3 sorting

def intersection(nums1, nums2):
    
    nums1.sort()
    nums2.sort()
    
    ptr1 = 0
    ptr2 = 0
    
    result = []
    
    while ptr1 < len(nums1) and ptr2 < len(nums2):
        if nums1[ptr1] == nums2[ptr2]:
            result.append(nums1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif nums1[ptr1] < nums2[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
            
    return list(set(result))

# Time Complexity : O(max(nlogn, mlogm)
# Space Complexity : O(n or m)