# Method-1

def findMaxAverage(nums, k):
    cur_sum = max_sum = sum(nums[:k])

    for i in range(0, len(nums)-k):
        cur_sum = cur_sum - nums[i] + nums[k+i]
        max_sum = max(max_sum, cur_sum)

    return max_sum / k

# Time Complexity : O(n)
# Space Complexity : O(1)