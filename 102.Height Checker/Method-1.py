# Method-1

def heightChecker(heights):
    length = len(heights)
    expected = sorted(heights)
    
    count = 0
    
    for i in range(length):
        if expected[i] != heights[i]:
            count += 1
            
    return count

# Time Complexity : O(nlogn)
# Space Complexity : O(1)

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

