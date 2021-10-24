# Method-1

def calculateTime(keyboard, word):

    start = 0
    time = 0
    for x in word:
        i = keyboard.find(x)
        time += abs(i - start)
        start = i
    return time

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: keyboard = "abcdefghijklmnopqrstuvwxyz",
# word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to 
# write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4.
