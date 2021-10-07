# Method-2 

def canBeTypedWords(text, brokenLetters):
    t = set(brokenLetters)
    count = 0
    
    for word in text.split():
        for char in word:
            if char in t:
                count += 1
                break
        
    return len(text.split()) - count

# Time Complexity : O(n * m)
# Space Complexity : O(m)