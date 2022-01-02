# Method-1

def groupAnagrams(strs):
    d = {}
    for w in strs:
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())

# Time Complexity : O(nlogn)
# Space Complexity : O(n)