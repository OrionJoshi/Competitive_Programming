# Method-1 Using Count function

def judgeCircle(moves):
    return ((moves.count('R') == moves.count('L')) & (moves.count('U') == moves.count('D')))

# Time Complexity : O(n)
# Space Complexity : O(1)


# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once.
# All moves have the same magnitude, so it ended up at the
# origin where it started. Therefore, we return true.