# Method-1

def maxPower(self, s: str) -> int:
    count = 0
    max_count = 0
    previous_chr = None

    for c in s:
        if c == previous_chr:
            count += 1
        else:
            previous_chr = c
            count = 1
        max_count = max(max_count, count)

    return max_count

# Time Complexity : O(n)
# Space Complexity : O(1)