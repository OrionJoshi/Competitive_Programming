# Method-1

def summaryRanges(nums):
    begin, res = 0, []

    for i in range(len(nums)):
        if i + 1 >= len(nums) or nums[i+1] - nums[i] != 1:
            b = str(nums[begin])
            e =  str(nums[i])
            res.append(b + "->" + e if b != e else b)
            begin = i + 1

    return res

# Time Complexity : O(n)
# Space Complexity : O(n)