# Method-1 Iterative Method

def minOperations(logs):
    count = 0
    
    for x in logs:
        if x == '../':
            if count > 0:
                count -= 1
        elif x == './':
            count = count
        else:
            count += 1
            
    return count

# Time complexity : O(n)
# Space Complexity : O(1)

# Input: logs = ["d1/","d2/","../","d21/","./"]
# Output: 2
# Explanation: Use this change folder operation "../" 2 times and go back to the main folder.