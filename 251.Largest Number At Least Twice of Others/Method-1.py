# Method-1

def dominantIndex(nums):
    a=max(nums)
    b=nums.index(a)

    for i in nums:
        if not a>=2*i and a!=i:
            return -1
    else:
        return b

# Time Complexity : O(n)
# Space Complexity : O(1)