# Method-1 Split and Join

def reverseWords(s):

    lst = s.split()
    
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
        
    return (' '.join(lst))

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"