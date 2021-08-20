# Method-1 Using Floyd's Tortoise and Hare (Cycle Detection)

def findDuplicate(nums):
    fast = nums[0]
    slow = nums[0]
    
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        
        if fast == slow:
            break
        
    fast = nums[0]
    
    while True:
        if fast == slow:
            break
        
        fast = nums[fast]
        slow = nums[slow]
        
    return fast

#  Time Complexity: O(n)
#  Space Complexity: O(1)
