# Method-2 using index

def reversePrefix(word, ch):
    if ch in word:
        ptr = word.index(ch)
        return word[ptr::-1] + word[ptr+1:]
    else:
        return word

# Time Complexity : O(n*n)
# Space Complexity : O(1)

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".