# Method-1

def goodDaysToRobBank(security, time):
    if time == 0:
        return [i for i in range(len(security))]
    
    if 2 * time >= len(security):
        return []
    
    before = 0
    after = 0
    good_days = []
    
    for idx in range(1, len(security) - time):
        before = before + 1 if security[idx-1] >= security[idx] else 0
        after = after + 1 if security[idx+time-1] <= security[idx+time] else 0
            
        if idx >= time and before >= time and after >= time:
            good_days.append(idx)
        
    return good_days

# Time Complexity : O(n)
# Space Complexity : O(n)