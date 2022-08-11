# Method-1

def wordBreak(s, wordDict):
    dictSet = set(wordDict)
    starts = [0]
    
    for i in range(len(s)):
        for j in starts:
            if s[j : i+1] in dictSet:
                starts.append(i+1)
                break
    
    return starts[-1] == len(s)

# Time Complexity : O(n^2)
# Space Complexity : O(n)