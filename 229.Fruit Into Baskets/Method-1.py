# Method-1

def totalFruit(fruits):
    start = 0
    end = 0
    mapping = {}
    count = 0

    while end < len(fruits):
        mapping[fruits[end]] = end

        if len(mapping) >= 3:
            minValue = min(mapping.values())
            del mapping[fruits[minValue]]
            start = minValue + 1
            
        count = max(count, end - start + 1)
        end += 1
    return count

# Time Complexity : O(n)
# Space Complexity : O(n)