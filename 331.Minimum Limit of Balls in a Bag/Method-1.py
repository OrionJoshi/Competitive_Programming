# Method-1

def minimumSize(nums, maxOperations):
    low, high = 1, max(nums)

    while low < high:
        mid=(low + high) >> 1
        if sum([(i-1) // (mid) for i in nums]) > maxOperations:
            low = mid + 1
        else:
            high = mid

    return low

# Time Complexity : O(logn)
# Space Complexity : O(1)