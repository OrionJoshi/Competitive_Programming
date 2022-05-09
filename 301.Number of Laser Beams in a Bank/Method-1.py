# Method-1

def numberOfBeams(bank):
    ans = prev = 0 
    for row in bank: 
        curr = row.count('1')
        if curr: 
            ans += prev * curr
            prev = curr 
    return ans 

# Time Complexity : O(n)
# Space Complexity : O(1)