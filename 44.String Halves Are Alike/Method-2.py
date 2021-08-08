# Method-2 Using List

def halvesAreAlike(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    lenHalf =  int(len(s) / 2)
    firstCount = 0
    secondCount = 0
    
    for i in range(0, lenHalf):
        if s[i] in vowels:
            firstCount += 1
        if s[i + lenHalf] in vowels:
            secondCount += 1
            
    return True if firstCount == secondCount else False

# Time Complexity : O(n)
# Space Complexity : O(1)