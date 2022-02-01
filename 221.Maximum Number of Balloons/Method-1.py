# Method-1

from collections import Counter

def maxNumberOfBalloons(text):
    countText = Counter(text)
    ballon = Counter('balloon')
    
    result = float('inf')
    for char in ballon:
        result = min(result, countText[char] // ballon[char])
        
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)