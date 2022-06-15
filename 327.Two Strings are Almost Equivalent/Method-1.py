# Method-1

def checkAlmostEquivalent(word1, word2):
    for i in word1:
        if abs(word1.count(i) - word2.count(i)) > 3:
            return False
    for j in word2:
        if abs(word1.count(j) - word2.count(j)) > 3:
            return False
    return True

# Time Complexity : O(n)
# Space Complexity : O(1)