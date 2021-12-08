# Method-1 hash table

from collections import Counter

def canConstruct(ransomNote, magazine):
    mapping = Counter(magazine)
            
    for i in range(len(ransomNote)):
        currentChr2 =  ransomNote[i]

        if currentChr2 not in mapping:
            return False
        else:
            if mapping[currentChr2] == 0:
                return False
            else:
                mapping[currentChr2] -= 1
                
    return True

# Time Complexity : O(n)
# Space Complexity : O(n)