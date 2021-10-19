# Method-1

def findKthPositive(arr, k):
    length = len(arr)
    
    if arr[-1] == length:
        return arr[-1] + k
        
    else:
        count = 0
        j = 0
        i = 1
        while True:
            print(i)
            if j < length and i == arr[j]:
                j += 1
            else:
                missingElement = i
                count += 1
                if count == k:
                    return missingElement
            i += 1

# Time Complexity : O(n + k)
# Space Complexity : O(1)

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers
# are [1,5,6,8,9,10,12,13,...]. 
# The 5th missing positive integer is 9.