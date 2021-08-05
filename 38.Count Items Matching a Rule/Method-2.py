# Method-2 using Hashing

def itemMatchingRule(items, ruleKey, ruleValue):
    
    mapping = {
        'type': 0,
        'color': 1,
        'name' : 2
    }
    
    return sum(1 for x in items if x[mapping[ruleKey]] == ruleValue)
    
# Time Complexity : O(n)
# Space Compelxity : O(1)    