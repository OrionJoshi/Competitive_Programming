# Method-1 Using pointers

def isStrobogrammatic(num):
    mapping = {"9": "6", "6": "9", "8": "8", "1": "1", "0": "0"}

    left = 0
    right = len(num) - 1
    
    while left <= right:
        if num[left] in mapping and mapping[num[left]] == num[right]:
            left += 1
            right -= 1            
        else:
            return False
    
    return True
    
# Time Complexity : O(n)
# Space Complexity : O(1)

#  Input: num = "69"
#  Output: true