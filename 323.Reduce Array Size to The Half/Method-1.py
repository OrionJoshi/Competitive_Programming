# Method-1

import collections

def minSetSize(arr):
    total_count = 0
    
    for index, count in enumerate(sorted(collections.Counter(arr).values(), reverse=True)):
        total_count += count
        
        if total_count >= len(arr) // 2:
            return index + 1
    
    return 0

# Time Complexity : O(nlogn)
# Space Complexity : O(n)