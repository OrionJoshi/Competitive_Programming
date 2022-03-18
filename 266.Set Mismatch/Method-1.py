# Method-1

def findErrorNums(nums):
    n = len(nums)
    true_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    set_sum = sum(set(nums))

    return [actual_sum - set_sum, true_sum - set_sum]

# Time Complexity : O(n)
# Space Complexity : O(1)