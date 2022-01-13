# Method-1

def rotate(nums, k):  
    k = k % len(nums)
    nums.reverse()
    nums[0: k] = nums[0: k][::-1]
    nums[k: len(nums)] = nums[k: len(nums)][::-1]

    return nums

# Time Complexity : O(n)
# Space Complexity : O(1)