# Method-1
import re
def numDifferentIntegers(word):
    word = re.findall('(\d+)', word)
    numbers = [int(i) for i in word]
    
    return len(set(numbers))

# Time Complexity : O(n)
# Space Complexity : O(n)