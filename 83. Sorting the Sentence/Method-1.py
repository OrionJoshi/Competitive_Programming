# Method-1

def sortSentence(s):
    temp = s.split()
    mapping = {}
    result = ''
    
    for i in temp:
        mapping[i[-1]] = i[:-1]
    for i in sorted(mapping):
        result = result + ''.join(mapping[i]) + ' '
    return result

# Time Complexity : O(n)
# Space Complexity : O(n + m)

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.