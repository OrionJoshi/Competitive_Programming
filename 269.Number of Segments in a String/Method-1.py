# Method-1

def countSegments(s):
    segment_count = 0

    for i in range(len(s)):
        if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
            segment_count += 1

    return segment_count

# Time Complexity : O(n)
# Space Complexity : O(1)