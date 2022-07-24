# Method-1

from collections import Counter

def closeStrings(word1, word2):
    dict1, dict2 = Counter(word1), Counter(word2)    

    if set(dict1.keys()) != set(dict2.keys()): 
        return False

    if sorted(dict1.values()) != sorted(dict2.values()): 
        return False

    return True

# Time Complexity : O(nlogn)
# Space Complexity : O(n)