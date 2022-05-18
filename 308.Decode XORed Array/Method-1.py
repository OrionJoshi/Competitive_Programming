# Method-1

def decode(encoded, first):
    r = [first]
    for i in encoded:
        r.append(r[-1] ^ i)

    return r

# Time Complexity : O(n)
# Space Complexity : O(n)