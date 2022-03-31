# Method-1

def pivotArray(nums, pivot):
    small_list = [item for item in nums if item < pivot]
    large_list = [item for item in nums if item > pivot]
    pivot_count = nums.count(pivot)
    
    return small_list + [pivot] * pivot_count + large_list

# Time Complexity : O(n)
# Space Complexity : O(n)