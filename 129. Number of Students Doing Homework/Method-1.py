# Method-1

def busyStudent(sTime, eTime, qTime):
    count = 0
    length = len(sTime)
    
    for i in range(length):
        if sTime[i] <= qTime <= eTime[i]:
            count += 1
            
    return count

# Time Complexity : O(n)
# Space Complexity : O(1)