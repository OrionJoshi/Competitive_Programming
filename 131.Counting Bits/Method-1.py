# Method-1 Dynamic programming

def countBits(n):
    
    result = [0]
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(result[i - 1] + 1)
        else:
            result.append(result[i // 2])
            
    return result


# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10