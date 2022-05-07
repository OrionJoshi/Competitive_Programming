# Method-1

def reorderSpaces(text):
    sp = text.count(' ')
    text = text.split()
    l = len(text) - 1
    x, y = divmod(sp, l) if l else (0, sp)

    return (' ' * x).join(text) + ' ' * y

# Time Complexity : O(n)
# Space Complexity : O(n)