# Method-1

def removeElement(nums, val):
    i=0
    for n in nums:
        if n!=val:
            nums[i]=n
            i+=1
    return i

# Time Complexity : O(n)
# Space Complexity : O(1)