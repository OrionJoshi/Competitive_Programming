# Method-1

from collections import Counter
from math import gcd
from functools import reduce

def hasGroupsSizeX(deck):
    if len(deck) < 2: return False
    return reduce(gcd, Counter(deck).values()) > 1

# Time Complexity : O(n)
# Space Complexity : O(1)