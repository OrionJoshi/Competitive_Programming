# Method-1

def subsets(nums):
    nums.sort()
    result = [[]]
    for num in nums:
        result += [i + [num] for i in result]
    return result

# Time Complexity : O(nlogn)
# Space Complexity : O(n)