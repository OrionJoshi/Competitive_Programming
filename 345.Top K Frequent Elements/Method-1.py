# Method-1

def topKFrequent(nums, k):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] = freq[num] + 1

    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    result = list(freq.keys())[:k]

    return result

# Time Complexity : O(nlogn)
# Space Complexity : O(n)