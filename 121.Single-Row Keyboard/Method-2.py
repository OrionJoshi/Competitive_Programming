# Method-2 Hash table

def calculateTime(keyboard, word):

    mapping = {}
    
    for i, c in enumerate(keyboard):
        mapping[c] = i
        
    start = 0
    time = 0
    
    for c in word:
        i = mapping[c]
        time += abs(i - start)
        start = i
        
    return time


# Time Complexity : O(n)
# Space Complexity : O(m) // m = 26