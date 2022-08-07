# Method-1

def nextGreaterElements(nums):
    stack, res, n = [], [-1] * len(nums), len(nums)
    
    for i in range(0, 2 * n):
        while stack and nums[i % n] > nums[stack[-1]]:
            top = stack.pop()
            if res[top] == -1:
                res[top] = nums[i % n]
        stack.append(i % n)
        
    return res

# Time Complexity : O(n)
# Space Complexity : O(n)