# Method-1

def getSumAbsoluteDifferences(nums):
    answer = []
    res = 0
    for i in range(1, len(nums)):
        res += nums[i] - nums[0]
    
    answer.append(res)
      
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        res += diff * (i - 1)
        res -= diff * (len(nums) - i - 1)
        
        answer.append(res)
    
    return answer

# Time Complexity : O(n)
# Space Complexity : O(n)