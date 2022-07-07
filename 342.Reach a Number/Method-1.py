# Method-1

def reachNumber(self, target: int) -> int:
    ans, k = 0, 0
    target = abs(target)
    while ans < target:
        ans += k
        k += 1
    while (ans - target) % 2:
        ans += k
        k += 1
    return k - 1

# Time Complexity : O(n)
# Space Complexity : O(1)