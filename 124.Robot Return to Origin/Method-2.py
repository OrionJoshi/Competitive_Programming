# Method-2 Iterative

def judgeCircle(moves):
    x = y = 0
    
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        else:
            x -= 1
    return x == y == 0

# Time Complexity : O(n)
# Space Complexity : O(1)