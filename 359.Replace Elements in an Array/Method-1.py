# Method-1

def arrayChange(nums, operations):
    dicts = {}

    for s, e in reversed(operations):
        dicts[s] = dicts[e] if e in dicts else e

    for i, num in enumerate(nums):
        if num in dicts:
            nums[i] = dicts[num]

    return nums

# Time Complexity : O(n)
# Space Complexity : O(n)