# Method-1

def carFleet(target, position, speed):
    n = len(position)
    time = [0] * n
    for i in range(n):
        time[i] = (target-position[i]) / speed[i]

    local = []
    for p,t in zip(position, time):
        local.append([p, t])

    local.sort()
    res = 1
    ma = local[n-1][1]

    for i in range(n-2, -1, -1):
        if local[i][1] > ma:
            ma = local[i][1]
            res+=1

    return res

# Time Complexity : O(nlogn)
# Space Complexity : O(n)